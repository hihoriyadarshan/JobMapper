from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [


    path('bloger',views.bloger,name='bloger'),
    path('adminblog',views.adminblog,name='adminblog'),
   



    ]