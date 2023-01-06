from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        # widgets={
        #     'username':forms.TextInput(attrs={
        #         'placeholder':'Username'
        #     }),

        #     'email':forms.TextInput(attrs={
        #         'placeholder':'email'
        #     }),

        #     'password1':forms.TextInput(attrs={
        #         'placeholder':'Password'
        #     }),
        #     'password2':forms.TextInput(attrs={
        #         'placeholder':'Re-enter Password'
        #     }),
        # }



class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields= ['customer','product','status']
        widgets={
            'customer':forms.Select(attrs={
                'class':'form-control'
            }),

            'product':forms.Select(attrs={
                'class':'form-control'
            }),

            'status':forms.Select(attrs={
                'class':'form-control'
            }),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields=['name','phone','email','picture']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'phone':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'picture':forms.FileInput(attrs={
                'class':'form-control form-control-sm',
            })
        }