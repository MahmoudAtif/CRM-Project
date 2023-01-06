from ast import arg
import re
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request , *args , **kwargs)

    return wrapper_func



def allowed_user(allowed_roles=[]):
    def decortores(view_func):
        def warpper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group =request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you are not autherized to this page')

        return warpper_func
    return decortores



def admin_page(view_func):
    def wrapper_func(request , *args , **kwargs):
        group=None
        if request.user.groups.exists():
            group= request.user.groups.all()[0].name

        if group =='customers':
            return redirect('user')
        
        if group=='admin':
            return view_func(request , *args , **kwargs)
    return wrapper_func   