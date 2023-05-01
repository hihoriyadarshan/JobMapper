from django.shortcuts import render
from django.urls import path
from . import views



urlpatterns = [


    path('bloger',views.bloger,name='bloger'),
    path('showbloger',views.showbloger,name='showbloger'),
    path('showbloger_company',views.showbloger_company,name='showbloger_company'),
    path('writeblog',views.writeblog,name='writeblog'),
    path('adminblog',views.adminblog,name='adminblog'),
    path('deleteblog<id>',views.deleteblog,name='deleteblog'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    path('adminLTE',views.adminLTE,name='adminLTE'),
    path('updateblog<id>',views.updateblog,name='updateblog'),
    path('editblog/<id>',views.editblog,name='editblog'),
    path('category',views.category,name='category'),
    path('add_category',views.add_category,name='add_category'),
    path('deletecategory<id>',views.deletecategory,name='deletecategory'),
    path('sup1',views.sup1,name='sup1'),
    path('company_data1',views.company_data1,name='company_data1'),
    path('showbloger_home',views.showbloger_home,name='showbloger_home'),
    path('admin_change_pswd',views.admin_change_pswd,name='admin_change_pswd'),
    path('change_password2',views.change_password2,name='change_password2'),
    path('uploadcsv',views.uploadcsv,name='uploadcsv'),
   

    
    # path('showcategory',views.showcategory,name='showcategory'),

    





  
    
    
    ]