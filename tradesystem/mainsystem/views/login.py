from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from mainsystem.models import Customer
# from mainsystem import utills
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        try:
            customer = Customer.get_Customer_by_email(email)
       
            if customer:
                customer = Customer.get_Customer_by_email(email)

                if password==customer.password:  
                    request.session['customer'] = customer.id
                    request.session['email'] = email
                    ####### main function call on new trade
                        # utills.Order_Angle.placeOrderApi(customer.broker_api,customer.broker_username,customer.broker_password)
                        # return HttpResponse("Login Successfully......")
                    return redirect('homepage')

                else:
                    error_message = 'Email Or Password invalid !!'
            else:
                error_message = 'Email Or Password invalid !!'

            # print(customer)
            # print(password)
        except Customer.DoesNotExist:
            error_message ='Email invalid !!!'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    print("Session Clear")
    request.session.clear()
    return render(request,'index.html')
    # return redirect('homepage')