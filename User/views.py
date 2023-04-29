from django.shortcuts import render
from User.forms import JobApplicationForm
from User.models import JobApplication
from SignUp.models import SignUp
from Company.models import jobpost
from django.contrib.auth.hashers import make_password ,check_password
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.
#user profile

def home(request):
    return render(request,'user-hp.html')

def jobapply_form(request):
    # j = jobpost.objects.get(job_id=id)
    # return HttpResponse(j)
    return render(request,'apply.html')


def jobapply(request): 
    # job = get_object_or_404(jobpost,job_id=id)   
    if request.method == "POST":
        form = JobApplicationForm(request.POST or None) 

        resume = " "
        if len(request.FILES) != 0:
          resume = str(request.FILES['resume'])

        j_id = request.session["job_id"]
        job = jobpost.objects.get(job_id= j_id) 
    
        jobapply.objects.create( 
            job_id = job, 
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            resume = request.FILES['resume']
            )

        return render (request, "apply.html")
    
        # a = request.POST.get("job_ids")
        # return HttpResponse(a) 
    # return HttpResponse(job) 
    # if request.method == "POST":
    #     a = request.POST.get("job_ids")
    #     job = get_object_or_404(jobpost,job_id=a)   
    #     return HttpResponse(job)
       
       

        if request.method == "GET":
            job = request.get["job_id"]
            return HttpResponse(job)
        company = jobpost.objects.get(job_id= job)  
        
        
    # return HttpResponse('Fail')


#chnage password user

def user_change_pswd(request):
    return render(request,'user_change_pswd.html')

def change_password1(request):
    if request.method == "POST":    
        old_pswd = request.POST.get("password")
        username1 = request.POST.get("username1")
    
        obj = get_object_or_404(SignUp, username = username1)
        
        result = check_password(old_pswd, obj.password)
        # if obj.companyname == 2 and result == True:
        if result == True:
        
            new_pswd = request.POST.get("new_password")
            cnfm_pswd = request.POST.get("cnfm_password")
            
            if new_pswd == cnfm_pswd:
                
                obj.password = make_password(new_pswd)
                obj.save()
                
                messages.success(request, "Password Changed successfully!")
                return render(request,'user_change_pswd.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'user_change_pswd.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'user_change_pswd.html')