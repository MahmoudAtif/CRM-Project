from pyexpat import model
from django import forms
import django_filters
from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields=['product','status']
        widgets={
            'product':forms.Select(attrs={
                'class':'form-control'
            }),
        }