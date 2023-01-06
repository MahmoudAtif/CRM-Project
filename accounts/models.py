from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
from itertools import product
import profile
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



# class Profile(models.Model):
#    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True , blank=True)
#    email=models.CharField(max_length=50,null=True , blank=True)
#    phone=models.CharField(max_length=50,null=True , blank=True)
#    picture=models.ImageField(default='avatar.png', null=True , blank=True)

#    def __str__(self):
#        return self.user 



class Customer(models.Model):
    user=models.OneToOneField(User, null=True , on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=50 , null=True)
    phone=models.CharField(max_length=50 , null=True)
    email=models.CharField(max_length=50 , null=True)
    picture=models.ImageField(null=True , blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Oudtdoor','Oudtdoor'),
    )
    name=models.CharField(max_length=50 , null=True)
    price=models.FloatField(max_length=10,null=True)
    category=models.CharField(max_length=50 , null=True, choices=CATEGORY)
    description=models.TextField(max_length=50 , null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)  
    tages=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Deliverd','Deliverd'),
    )
    customer=models.ForeignKey(Customer,null=True, on_delete=models.CASCADE, related_name='order')
    product=models.ForeignKey(Product,null=True, on_delete=models.CASCADE,related_name='order')
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50 , null=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name
