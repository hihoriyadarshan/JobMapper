from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [

    path('',views.homepage,name='home'),

    path('sign_up',views.sign_up,name='sign_up'),
    path('signup',views.signup,name='signup'),
    path('sup',views.sup,name='signup_data'),
    
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('loginHandleAdmin',views.loginHandleAdmin,name='loginHandleAdmin'),
    path('loginHandlecompany',views.loginHandlecompany,name='loginHandlecompany'),
    path('admin_data',views.admin_data,name='admin_data'),
    path('loginHandle',views.loginHandle,name='loginHandle'),
    path('companylogin',views.companylogin,name='companylogin'),
    path('company',views.company,name='company'),
    path('company_data',views.company_data,name='company_data'),
    path('logout',views.logout,name='logout'),
    path('cont',views.cont,name='contact_data'),
    path('feedback',views.feedback,name='feedback'),
    path('showcontact',views.showcontact,name='showcontact'),
    path('deletemessage<id>',views.deletemessage,name='deletemessage'),
    path('comapanyhomepage',views.companyhomepage,name='comapanyhomepage'),
    path('user',views.user,name='user'),
    path('showcompany',views.showcompany,name='showcompany'),
    path('showuser',views.showuser,name='showuser'),
    
    path('deleteuser<id>',views.deleteuser,name='deleteuser'),
    path('updateuser<id>',views.updateuser,name='updateuser'),
    path('edituser/<id>',views.edituser,name='edituser'),
    
    path('deletecompany<id>',views.deletecompany,name='deletecompany'),
    path('updatecompany<id>',views.updatecompany,name='updatecompany'),
    path('editcompany/<id>',views.editcompany,name='editcompany'),

    path('showprofile',views.showprofile,name='showprofile'),
    path('showcompanyprofile',views.showcompanyprofile,name='showcompanyprofile'),
    path('create-pdf',views.user_pdf_report,name='create-pdf'),
    path('home_page',views.home_page,name='home_page'),
    path('admin_signup',views.admin_signup,name='admin_signup'),



   

    
    
    



]