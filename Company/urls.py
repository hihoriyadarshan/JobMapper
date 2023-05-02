from django.shortcuts import render
from django.urls import path
from . import views



urlpatterns = [
       path('companyhomepage',views.companyhomepage,name='companyhomepage'),
       path('companyfeedback',views.companyfeedback,name='companyfeedback'),
       path('showcompanyfeedback',views.showcompanyfeedback,name='showcompanyfeedback'),
       path('jobpost_data',views.jobpost_data,name='jobpost_data'),
       path('job_post',views.job_post,name='job_post'),
       path('jobpost_datacsvdownload',views.jobpost_datacsvdownload,name='jobpost_datacsvdownload'),

       path('showjobpost',views.showjobpost,name='showjobpost'),      
      
       path('showjob',views.showjob,name='showjob'),      
      
       path('deletecompanyfeedback/<id>',views.deletecompanyfeedback,name='deletecompanyfeedback'),
       path('deletejobpost<job_id>',views.deletejobpost,name='deletejobpost'),
       path('joblist',views.joblist,name='joblist'),
       path('showjob1',views.showjob1,name='showjob1'),
       path('company_change_pswd',views.company_change_pswd,name='company_change_pswd'),
       path('change_password',views.change_password,name='change_password'),
       # path('job_upload',views.job_upload,name='job_upload'),
       path('jobpost_csv_upload<companyname>',views.jobpost_csv_upload,name='jobpost_csv_upload'),
       



       


    
]