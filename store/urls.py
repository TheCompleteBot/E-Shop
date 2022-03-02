
from django.contrib import admin
from django.urls import path
from .views import index,SignUp,login,vendsingup,logout,cart
urlpatterns = [
    path('',index,name='Index'),
    path('signup',SignUp,name='SignUp'),
    path('login',login,name='Login'),
    path('vendsignup',vendsingup , name = 'VENDORSIGNUP'),
    path('logout',logout,name='logout'),
    path('cart',cart,name='cart')
]
