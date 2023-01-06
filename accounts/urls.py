from re import template
from django.urls import path

from . import views

from django.contrib.auth import views as authViews

urlpatterns=[
    path('',views.home,name='home'),
    path('products',views.products,name='products'),
    path('customers/<int:pk_test>/',views.customers,name='customers'),
    path('createOrder/<int:pk_test>/',views.createOrder,name='createOrder'),
    path('createCustomer',views.createCustomer,name='createCustomer'),
    path('update/<int:pk_test>',views.update, name='update'),
    path('delete/<int:pk_test>',views.delete,name='delete'),
    path('updateprofile/<int:pk_test>',views.updateProfile,name='updateprofile'),
    
    path('login',views.loginPage,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logoutuser,name='logout'),

    path('user',views.user,name='user'),
    path('profile/<str:name>',views.profile,name='profile'),


    # template_name='accounts/password_reset.html'
    # path('PasswordResetView',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('PasswordResetDoneView',auth_views.PasswordResetDoneView.as_view(),name=' password_reset_done'),
    # path('PasswordResetConfirmView/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name=' password_reset_confirm'),
    # path('PasswordResetCompleteView',auth_views.PasswordResetCompleteView.as_view(),name=' password_reset_complete'),


     path('reset_password/' ,authViews.PasswordResetView.as_view() , name="reset_password"),
     path('reset_password_sent/' ,authViews.PasswordResetDoneView.as_view() , name="password_reset_done"),
     path('reset/<uidb64>/<token>/' ,authViews.PasswordResetConfirmView.as_view() , name="password_reset_confirm"),
     path('reset_password_complete/' ,authViews.PasswordResetCompleteView.as_view() , name="password_reset_complete"),
]
