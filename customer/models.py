from django.db import models
from .models import *
from seller .models import *
# Create your models here.
class Customer(models.Model):
    username=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
    email=models.EmailField(null=True)

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveBigIntegerField(default=1)

class Wishlist(models.Model):
    customers=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

   
    

