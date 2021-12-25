from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from mainsystem.models import Customer
import logging

# from importlib import reload
# logger  = logging.getLogger(__name__)
class Index(View):
    
    def get(self,request):
        
        if request.session.get('email')!=None:
            email=request.session['email']
            customer = Customer.get_Customer_by_email(email)
            client = customer.broker_username
            return render(request, 'index.html',{'client':client})
            
        else:
            # return HttpResponse("done")
            return render(request, 'index.html')
        