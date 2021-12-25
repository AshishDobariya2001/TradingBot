from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    broker_name = models.CharField(max_length=50)
    broker_username = models.CharField(max_length=50)
    broker_password = models.CharField(max_length=500)
    broker_api = models.CharField(max_length=80)
    password = models.CharField(max_length=500)

    def ragister(self):
        self.save()

    def get_Customer_by_email(email):
        return Customer.objects.get(email=email)

    def isExists(self):
        if Customer.objects.filter(email =self.email):
            return True

class Order_info(models.Model):   
    email = models.EmailField(max_length=50)
    broker_username = models.CharField(max_length=20)

    orderId = models.IntegerField()
    variety = models.CharField(max_length=20)
    tradingsymbol = models.CharField(max_length=50)
    transactiontype = models.CharField(max_length=10)
    exchange = models.CharField(max_length=10)
    ordertype = models.CharField(max_length=30)
    producttype = models.CharField(max_length=20)
    duration = models.CharField(max_length=10)
    quantity = models.IntegerField()
    timedate = models.DateTimeField()

    def ragister(self):
        self.save()
    
    def get_order_by_email(email):
        return Order_info.objects.filter(email = email).order_by('-timedate')