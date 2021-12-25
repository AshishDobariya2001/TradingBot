from django.views import View
from django.shortcuts import redirect, render
# from mainsystem import utills
import datetime
from mainsystem.models import Customer,Order_info
from django.shortcuts import render
from django.http.response import HttpResponse
# from mainsystem.tasks import test_func
from celery.schedules import crontab
# from django.http.response import HttpResponse
from django.shortcuts import render
# from .tasks import test_func
from mainsystem.tasks import placeOrderApi
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# from celery import shared_task
# import time


class Order_details(View):
    
    def get(self, request):
        
        email = request.session['email']
        order = Order_info.get_order_by_email(email)

        date_info = datetime.date.today()
        
        customer = Customer.get_Customer_by_email(email)
        client = customer.broker_username
        print(date_info)
        return render(request, 'OrderDetails.html',{'order' : order,'email': email,'date':date_info,'client':client})

    def post(self, request):
        time_order = email = request.POST.get('time')
        
        email = request.session['email']
        print(email)
        customer = Customer.get_Customer_by_email(email)
        print(customer)
        # time_order =datetime(time_order)
        
        date_time_obj = datetime.datetime.strptime(time_order, '%H:%M')
        print(type(date_time_obj))
        print('Hour :',date_time_obj.hour)
        h = date_time_obj.hour
        mint = date_time_obj.minute
        print(h,mint)
        # request.session['time'] = time
        
        
        print(time_order)
        
        schedule, created = CrontabSchedule.objects.get_or_create(hour = h, minute = mint,day_of_month=7,month_of_year=12)
        task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"14", task='mainsystem.tasks.placeOrderApi', args = json.dumps((customer.broker_api,customer.broker_username,customer.broker_password,customer.email,)))
        # # return HttpResponse("Done")
        # utills.Order_Angle.placeOrderApi(customer.broker_api,customer.broker_username,customer.broker_password,customer.email)
        
        # print(time)
        customer = Customer.get_Customer_by_email(email)
        client = customer.broker_username
        order = Order_info.get_order_by_email(email)
        print("Success post method.....................")
        return render(request, 'OrderDetails.html',{'order' : order,'email': email,'client':client})
    
    # @shared_task
    # def OrderPlace():
    #     time.sleep(10)
    #     print("Order Placed")
        