from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)
    quantity=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    
class Seller(models.Model):
    username=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
    email=models.EmailField(null=True)