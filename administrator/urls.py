from django.shortcuts import render
from django.urls import path
from . import views



urlpatterns = [


    path('bloger',views.bloger,name='bloger'),
    path('showbloger',views.showbloger,name='showbloger'),
    path('showbloger_company',views.showbloger_company,name='showbloger_company'),
    path('adminblog',views.adminblog,name='adminblog'),
    path('deleteblog<id>',views.deleteblog,name='deleteblog'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    path('adminLTE',views.adminLTE,name='adminLTE'),
    # path('showcontact',views.showcontact,name='showcontact'),

    path('companyuser_pdf', views.companyuser_pdf, name='companyuser_pdf'),


    #pdf
    

   

    
    ]