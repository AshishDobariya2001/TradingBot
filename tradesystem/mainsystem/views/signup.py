from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from mainsystem.models import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        f_name = postData.get('f_name')
        email = postData.get('email')
        broker_name=postData.get('broker_name')
        broker_username = postData.get('username')
        broker_password = postData.get('broker_password')
        broker_api = postData.get('api')
        gender = postData.get('gender')
        password = postData.get('password')
        
        value={
            'f_name':f_name,
            'email' :email,
            'broker_name':broker_name,
            'broker_api':broker_api
        }
        print(f_name,email ,broker_name,broker_username,broker_password,broker_api,password)
        customer = Customer(
                            name=f_name,
                            email = email,
                            broker_name=broker_name,
                            broker_username=broker_username,
                            broker_password = broker_password,
                            broker_api = broker_api,
                            password= password
                            )
        # customer.ragister()
        error_message = self.validateCustomer(customer)
        # validation

        if not error_message:
            # customer.password = make_password(customer.password)
            customer.ragister()
            print("commit")
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        
        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if (not customer.name):
            error_message = "Name Required..!!"
        elif len(customer.name) < 4:
            error_message = "frist name is more than 4 Charactor"
        elif not customer.email:
            error_message = "email must be required..!!"
        elif len(customer.password) < 6:
            error_message = "Password must be more than 6 char Long"
        elif not customer.broker_name:
            error_message = "Please Select Broker-name...!! "
        elif not customer.broker_username:
            error_message = "Please Enter Username...!!"
        elif not customer.broker_password:
            error_message = "Please Enter Broker Password"
        elif not customer.broker_api:
            error_message = "Please Enter Broker API Link..!!"
        elif customer.isExists():
            error_message = 'Email Address Already Registered..!!'

        return error_message
