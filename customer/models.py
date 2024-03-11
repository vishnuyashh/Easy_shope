from django.db import models

# Create your models here.
class Customer(models.Model):
    username=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
    email=models.EmailField(null=True)

# class Cart(models.Model):
#     customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
#     product=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
#     price=models.ForeignKey()

    

