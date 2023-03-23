from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [


    path('bloger',views.bloger,name='bloger'),
    path('adminblog',views.adminblog,name='adminblog'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    path('adminLTE',views.adminLTE,name='adminLTE'),
    path('deleteblog<id>',views.deleteblog,name='deleteblog'),
    # path('showcontact',views.showcontact,name='showcontact'),
    path('feedback',views.feedback,name='feedback'),


   

    
    ]