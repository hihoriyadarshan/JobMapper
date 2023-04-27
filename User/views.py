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