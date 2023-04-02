from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
       path('companyhomepage',views.companyhomepage,name='companyhomepage'),
       path('companyfeedback',views.companyfeedback,name='companyfeedback'),
       path('showcompanyfeedback',views.showcompanyfeedback,name='showcompanyfeedback'),

       # path('cont1',views.cont1,name='contact_data'),
    
]