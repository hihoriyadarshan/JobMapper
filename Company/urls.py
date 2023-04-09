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
       # path('deletecompanyfeedback<id>',views.deletecompanyfeedback,name='deletecompanyfeedback'),
       path('deletecompanyfeedback<id>',views.deletecompanyfeedback,name='deletecompanyfeedback'),
       


    
]