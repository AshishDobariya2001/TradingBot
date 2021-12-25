from django.contrib import admin
from .models import Customer,Order_info

# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','email', 'broker_username']



class AdminOrder(admin.ModelAdmin):
    list_display = ['email','broker_username','orderId']


# Register your models here.
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order_info , AdminOrder)
