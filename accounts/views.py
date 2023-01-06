from ast import Return
from django.contrib.auth.models import Group
from multiprocessing import context
from time import sleep
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .decorators import *
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.

# @allowed_user(allowed_roles=['admin'])


@login_required(login_url='login')
@admin_page
def home(request):
    orders=Order.objects.all()
    total_orders= orders.count()
    oreders_deliverd_count=Order.objects.filter(status='Deliverd').count()
    oreders_pending_count=Order.objects.filter(status='Pending').count()
    customers=Customer.objects.all()
    # customers_order=customers.order.all()
    
    context={
        'orders':orders,
        'total_orders':total_orders,
        'deliverd_count':oreders_deliverd_count,
        'pending_count':oreders_pending_count,
        'customers':customers,
    }
    return render(request , 'accounts/dashboard.html',context)


@login_required(login_url='login')
def products(request):
    products=Product.objects.all()
    context={
        'products':products,
    }
    return render(request , 'accounts/products.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customers(request,pk_test):

    customer=Customer.objects.get(id=pk_test)
    orders=customer.order.all()
    total_orders=orders.count()
    
    filterForm=OrderFilter()
    if request.method =='GET':
        filterForm=OrderFilter(request.GET,queryset=orders)
        orders=filterForm.qs
    
    context={
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
        'filterForm':filterForm,
    }
    
    return render(request , 'accounts/customers.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createOrder(request,pk_test):

    OrderFormSet=inlineformset_factory(Customer,Order, fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk_test)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form= OrderForm(initial={'customer':customer})
    if request.method=='POST':
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
            
    context={
        'form':formset
    }
    return render(request,'accounts/CreateOrder.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createCustomer(request):
    form =CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={
        'form':form
    }
    return render(request,'accounts/CreateCustomer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update(request,pk_test):
    order_id=Order.objects.get(id=pk_test)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=OrderForm(instance=order_id)

    context={
        'form':form
    }

    return render(request,'accounts/update.html',context)

@login_required(login_url='login')
# @allowed_user(allowed_roles=['admin'])
def delete(request, pk_test):
    order=Order.objects.get(id=pk_test)
    if request.method=='POST':
        order.delete()
        return redirect('home')

    return render(request,'accounts/delete.html')
    


@unauthenticated_user
def loginPage(request):
        
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password incorrect')

    
    context={
        
    }
    return render(request , 'accounts/login.html',context)

@unauthenticated_user
def register(request):
    
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,' Success registeration for '+username)
            return redirect('login')

    context = {
        'form':form,
    }
    return render(request , 'accounts/register.html',context)


def logoutuser(request):
     logout(request)
     return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_roles='customers')
def user(request):
    users=request.user.customer
    order=users.order.all()
    total_orders=order.count()
    oreders_deliverd_count=order.filter(status='Deliverd').count()
    oreders_pending_count=order.filter(status='Pending').count()
    context={
        'orders':order,
        'total_orders':total_orders,
        'deliverd_count':oreders_deliverd_count,
        'pending_count':oreders_pending_count
    }
    return render(request, 'accounts/user.html',context)




# @allowed_user(allowed_roles=["customers"])
def profile(request,name):

    user=request.user.customer
    # customer_name=Customer.objects.get(username=name)
    if request.method =='POST':
        form=CustomerForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    else:
        form=CustomerForm(instance=user)
    context={
        "form":form,
    }
    return render(request, 'accounts/profile.html',context)



def updateProfile(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    if request.method =='POST':
        form = CustomerForm(request.POST ,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    else:
        form=CustomerForm(instance=customer)
   
    context={
        'customer':customer,
        'form':form
    }
    return render(request, 'accounts/updateprofile.html',context)
