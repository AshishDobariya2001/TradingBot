from mainsystem.models import Customer, Order_info
from datetime import datetime, date
import math
import pandas as pd
import requests
from smartapi import SmartConnect
from celery import shared_task
from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from tradesystem import settings
from django.utils import timezone
from datetime import timedelta
import warnings
from requests.api import request
from django.shortcuts import redirect

warnings.filterwarnings('ignore')  # ignore the warning


# @shared_task(bind=True)
# def test_func(self):
#     # operations
#     for i in range(10):
#         print(i)
#     return "Done"


@shared_task(bind=True)
def placeOrderApi(self,key, username, pwd, email):
    apikey = key
    username = username
    pwd = pwd

    def trading():
        obj = SmartConnect(api_key=apikey)  # get the object of api
        data = obj.generateSession(username, pwd)
        data

        obj.position()  # get current position of our fno trade

        # obj.ltpData('NFO','BANKNIFTY30SEP21FUT','48506')

        def place_order(token, symbol, qty, buy_sell, ordertype, price, variety='NORMAL', exch_seg='NSE', triggerprice=0):
            try:
                orderparams = {
                    "variety": variety,
                    "tradingsymbol": symbol,
                    "symboltoken": token,
                    "transactiontype": buy_sell,
                    "exchange": exch_seg,
                    "ordertype": ordertype,
                    "producttype": "INTRADAY",
                    "duration": "DAY",
                    "price": price,
                    "squareoff": "0",
                    "stoploss": "0",
                    "quantity": qty,
                    "triggerprice": triggerprice
                }
                print(orderparams)
                orderId = obj.placeOrder(orderparams)
                # email = request.session['email']

                timedate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print("The order id is: {}".format(orderId))
                order = Order_info(
                    email=email,
                    broker_username=username,
                    orderId=orderId,
                    variety=orderparams['variety'],
                    tradingsymbol=orderparams['tradingsymbol'],
                    transactiontype=orderparams['transactiontype'],
                    exchange=orderparams['exchange'],
                    ordertype=orderparams['ordertype'],
                    producttype=orderparams['producttype'],
                    duration=orderparams['duration'],
                    quantity=orderparams['quantity'],
                    timedate=timedate
                )
                # print(order)
                order.ragister()
            except Exception as e:
                print("Order placement failed: {}".format(e.message))

            def demo():
                print("ritul")
                a = obj.tradeBook()
                b = a['data']
                sl1 = b[0]
                sl2 = b[1]
                fillprize1 = sl1['fillprice']
                fillprize2 = sl2['fillprice']
                place_order(ce_strike_symbol['token'], ce_strike_symbol['symbol'],
                            ce_strike_symbol['lotsize'], 'BUY', 'STOPLOSS_LIMIT', 0, 'NORMAL', 'NFO', fillprize1+40)
                place_order(ce_strike_symbol['token'], ce_strike_symbol['symbol'],
                            ce_strike_symbol['lotsize'], 'BUY', 'STOPLOSS_LIMIT', 0, 'NORMAL', 'NFO', fillprize2+40)

        url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
        d = requests.get(url).json()
        token_df = pd.DataFrame.from_dict(d)
        token_df['expiry'] = pd.to_datetime(
            token_df['expiry']).apply(lambda x: x.date())
        token_df = token_df.astype({'strike': float})
        token_df

        def getToken(symbol, exch_seg='NSE', instrumenttype='OPTIDX', strike_price='', pe_ce='CE', expiry_day=None):
            df = token_df
            strike_price = strike_price*100
            if exch_seg == 'NSE':
                eq_df = df[(df['exch_seg'] == 'NSE')]
                return eq_df[eq_df['name'] == symbol]
            elif exch_seg == 'NFO' and ((instrumenttype == 'FUTSTK') or (instrumenttype == 'FUTIDX')):
                return df[(df['exch_seg'] == 'NFO') & (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol)].sort_values(by=['expiry'])
            elif exch_seg == 'NFO' and (instrumenttype == 'OPTSTK' or instrumenttype == 'OPTIDX'):
                return df[(df['exch_seg'] == 'NFO') & (df['expiry'] == expiry_day) & (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol) & (df['strike'] == strike_price) & (df['symbol'].str.endswith(pe_ce))].sort_values(by=['expiry'])

        expiry_day = date(2021, 12, 9)

        symbol = 'BANKNIFTY'

        spot_token = getToken(symbol).iloc[0]['token']
        ltpInfo = obj.ltpData('NSE', symbol, spot_token)
        indexLtp = ltpInfo['data']['ltp']
        indexLtp

        ATMStrike = math.ceil(indexLtp/100)*100
        print(ATMStrike)

        # ATMStrike1=ATMStrike+1200
        # ATMStrike2=ATMStrike-1200

        ce_strike_symbol = getToken(
            symbol, 'NFO', 'OPTIDX', ATMStrike, 'CE', expiry_day).iloc[0]
        # ce_strike_symbol1=getTokenInfo(symbol,'NFO','OPTIDX',ATMStrike1,'CE',expiry_day).iloc[0]

        pe_strike_symbol = getToken(
            symbol, 'NFO', 'OPTIDX', ATMStrike, 'PE', expiry_day).iloc[0]
        # pe_strike_symbol1=getTokenInfo(symbol,'NFO','OPTIDX',ATMStrike2,'PE',expiry_day).iloc[0]

        place_order(ce_strike_symbol['token'], ce_strike_symbol['symbol'],
                    ce_strike_symbol['lotsize'], 'SELL', 'MARKET', 0, 'NORMAL', 'NFO')
        # place_order(ce_strike_symbol1['token'],ce_strike_symbol1['symbol'],ce_strike_symbol1['lotsize'],'BUY','MARKET',0,'NORMAL','NFO')

        place_order(pe_strike_symbol['token'], pe_strike_symbol['symbol'],
                    pe_strike_symbol['lotsize'], 'SELL', 'MARKET', 0, 'NORMAL', 'NFO')
        # place_order(pe_strike_symbol1['token'],pe_strike_symbol1['symbol'],pe_strike_symbol1['lotsize'],'BUY','MARKET',0,'NORMAL','NFO')
        # demo()
    trading()
    # return redirect('orderpage')
    
