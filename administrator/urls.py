from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [

    # path('blogpage',views.blogpage,name='blogpage'),
    path('bloger',views.bloger,name='bloger'),

    ]