from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('home',views.home,name='home'),
    path('jobapply_form/<id>', views.jobapply_form,name='jobapply_form'), 
    #path('user_jobapply', views.user_jobapply,name='user_jobapply'),           
    path('user_change_pswd',views.user_change_pswd,name='user_change_pswd'),
    path('change_password1',views.change_password1,name='change_password1'),
]