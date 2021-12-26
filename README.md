# TradingBot
Algorithmic trading (also called automated trading, black-box trading, or algo-trading) uses a computer program that follows a defined set of instructions (an algorithm) to place a trade.

# Required library
1. pip install pandas
2. pip install smartapi-python
3. pip install websocket
4. pip install celery
5. pip install django_celery_results
6. pip install django_celery_beat
7. pip install requests

Django server run

python manage.py runserver

Run celery server 

celery -A tradesystem.celery worker --pool=solo -l info

Run celery beat server

celery -A tradesystem beat -l info

# Abstract 

Algorithmic trading has been blamed for an increasing level of volatility in a number of 
financial markets. Adoption and deployment of algorithmic trading systems has increased 
and this is likely to continue, as regulation, competition and innovation drive the 
development of advanced technological tools. Expert and intelligent systems provide the 
mechanics for both reacting to and affecting a financial market that is now significantly 
faster and operating across multiple time zones and markets. Surprisingly, much of this 
innovation has escaped discussion within the Information Systems research community. 


