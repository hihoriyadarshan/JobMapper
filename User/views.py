from django.shortcuts import render
from User.forms import JobApplicationForm
from User.models import JobApplication
from Company.models import jobpost

from django.http import HttpResponse

# Create your views here.
#user profile

def home(request):
    return render(request,'user-hp.html')

def jobapply1(request):
    return render(request,'apply.html')


def jobapply(request):  
    if request.method == "POST":

        # job = request.session["job_id"]
        # company = jobpost.objects.get(job_id= job) 
        form = JobApplicationForm(request.POST or None) 
       
        resume = " "
        if len(request.FILES) != 0:
          resume = str(request.FILES['resume'])
         
        # return HttpResponse(image)
           
        job = request.session["job_title"]
        return HttpResponse(job)
        company = jobpost.objects.get(job_id= job)  
        
        jobapply.objects.create( 
        job_id = company, 
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        resume = resume
        )

    return render (request, "apply.html")
    # return HttpResponse('Fail')
