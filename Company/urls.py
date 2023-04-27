from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
       path('companyhomepage',views.companyhomepage,name='companyhomepage'),
       path('companyfeedback',views.companyfeedback,name='companyfeedback'),
       path('showcompanyfeedback',views.showcompanyfeedback,name='showcompanyfeedback'),
       path('jobpost_data',views.jobpost_data,name='jobpost_data'),
       path('job_post',views.job_post,name='job_post'),
       # path('job_post1',views.job_post1,name='job_post1'),

       path('showjobpost',views.showjobpost,name='showjobpost'),      
       path('showjob',views.showjob,name='showjob'),      
       path('deletecompanyfeedback/<id>',views.deletecompanyfeedback,name='deletecompanyfeedback'),
       path('deletejobpost<job_id>',views.deletejobpost,name='deletejobpost'),
       path('joblist',views.joblist,name='joblist'),
       path('showjob1',views.showjob1,name='showjob1'),
       path('company_change_pswd',views.company_change_pswd,name='company_change_pswd'),
       path('change_password',views.change_password,name='change_password'),
       


    
]