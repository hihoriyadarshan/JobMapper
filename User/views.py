from django.shortcuts import render

# Create your views here.
#user profile

def home(request):
    return render(request,'user-hp.html')

