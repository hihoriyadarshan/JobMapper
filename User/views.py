from django.shortcuts import render
from User.forms import JobApplicationForm
from User.models import JobApplication
from SignUp.models import SignUp
from Company.models import jobpost
from django.contrib.auth.hashers import make_password ,check_password
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.
#user profile

def home(request):
    return render(request,'user-hp.html')

def jobapply_form(request,id):
    job = jobpost.objects.get(job_id=id)
    if request.method == 'POST':
        # Process the form data and save it to the JobApplication model
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        application = JobApplication(job=job, name=name, email=email, resume=resume)
        application.save()
        # Redirect to a success page
        return redirect('application_success')
    else:
        # Render the apply.html template with the job details
        context = {'job': job}
        return render(request, 'apply.html', context)



# def user_jobapply(request):   
#     if request.method == "POST":
#         # a = request.POST.get('job_id')
#         # return HttpResponse(a)
        

#         return HttpResponse('Fail')
#         return render (request, "apply.html")


# def user_jobapply(request,job_id):
#     job = jobpost.objects.get(pk=job_id)
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.job_post = job
#             application.save()
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = JobApplicationForm()
#     context = {'job': job, 'form': form}
#     return render(request, 'apply.html', context)
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
                return render(request,'userprofile.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'user_change_pswd.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'user_change_pswd.html')