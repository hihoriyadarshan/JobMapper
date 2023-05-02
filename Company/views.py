from django.shortcuts import render,redirect,get_object_or_404
from Company.forms import company_contactForm,jobpostForm
from Company.models import company_contact,jobpost
from django.core.paginator import Paginator
from SignUp.models import Company
from django.contrib.auth.hashers import make_password ,check_password
from django.contrib import messages
import pandas as pd
import io
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import chardet
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template




# """ Insert Games using CSV upload """
def jobpost_csv_upload(request,companyname):
    return HttpResponse(companyname)
    context = Company.objects.get(companyname=companyname)
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        if file_name.endswith('.csv'):
            # For CSV files, read the file directly
            raw_data = uploaded_file.read()
            # Detect the encoding of the file
            file_encoding = chardet.detect(raw_data)['encoding']
            # Decode the file using the detected encoding
            decoded_data = raw_data.decode(file_encoding)
            # Create a StringIO object for pandas to read from
            file_stream = io.StringIO(decoded_data)
            df = pd.read_csv(file_stream)
        elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            # For Excel files, use pandas to read the file
            df = pd.read_excel(io.BytesIO(uploaded_file.read()))
        else:
            messages.error(request, 'File is not a CSV or Excel file')
            return render(request, "csvupload.html")

        # Loop through each row in the DataFrame and create a new instance of YourModel
        for index, row in df.iterrows():
            # Check for any primary key or unique constraints
            try:
                obj = jobpost.objects.create(
                    companyname            = row['companyname'],
                    job_title              = row['job_title'],
                    salary                 =row['salary'],
                    experience_required    = row['experience_required'],
                    jobtype                = row['jobtype'],
                    skill_required         = row['skill_required'],
                    education_level        = row['education_level'],
                    last_date              = row['last_date'],
                    job_description        = row['job_description'],



                )
            except ValidationError as e:
                # Handle any validation errors
                messages.error(request, f"Error creating object: {str(e)}")
                return render(request, "csvupload.html")
                
                # return redirect(reverse(jobpost_csv_upload),{'context' : context})
            except IntegrityError as e:
                # Handle any duplicate primary key or unique constraint errors
                messages.error(request, f"Error creating object: {str(e)}")
                return render(request, "csvupload.html")
             
                # return redirect(reverse(jobpost_csv_upload))
        messages.success(request, 'CSV file uploaded successfully')
        return render(request, "csvupload.html")
    return render(request, "csvupload.html")

        # return redirect(reverse(jobpost_csv_upload))
    # return redirect(reverse(jobpost_csv_upload))




def companyhomepage(request):
    return render(request,"companyhomepage.html")

def job_post(request):
        return render(request,'jobpost.html')

def joblist(request):
        return render(request,'job list.html')



# Create your views here.
def companyfeedback(request):  
   
    if request.method == "POST": 
        
        form = company_contactForm(request.POST or None) 
        
        if form.is_valid():
            
            try:  
                form.save()  
                return render(request,'home.html')  
            except:  
                pass  
    else:  
        form = company_contactForm()  
    return render(request,'companyhomepage.html',{'form':form})

#show contact

def showcompanyfeedback(request):
    company = company_contact.objects.all()
    p = Paginator(company, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj} 
    return render(request,'companyfeedback.html',context)

#delete company feedback

def deletecompanyfeedback(request,id):
    # return HttpResponse(id)

    context = {}
    obj = get_object_or_404(company_contact,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showcompanyfeedback")
    return render(request, "companyfeedback.html", context)


#job post 


def jobpost_data(request):  
    if request.method == "POST": 

        form = jobpostForm(request.POST or None) 

       
        image = " "
        if len(request.FILES) != 0:
          image = str(request.FILES['image'])
         
        # return HttpResponse(image)
           
        companyins = request.session["companyname"]
        company = Company.objects.get(companyname= companyins)  
        
        jobpost.objects.create( 
        companyname = company,  
        job_title = request.POST.get('job_title'),
        salary = request.POST.get('salary'),
        jobtype = request.POST.get('jobtype'),
        experience_required = request.POST.get('experience_required'),
        education_level = request.POST.get('education_level'),
        skill_required = request.POST.get('skill_required'),  
        job_description = request.POST.get('job_description'),
        post_date = request.POST.get('Endtime'),
        last_date = request.POST.get('Enddate'),
        image = request.FILES['image']
        )
      
        

    
    return render (request, "jobpost.html")


# jobpost_data csv download
def jobpost_datacsvdownload(request):
    
    file_open = open("jobpost_data.csv", "a")

    for company in jobpost.objects.all():
        file_open.write(str(company.job_id)+ "," +str(company.job_title)+ "," +str(company.jobtype)+ "," +str(company.education_level)+ "," +str(company.skill_required)+ "," +str(company.experience_required)+ "," +str(company.salary)+ "," +str(company.companyname.companyname)
 +  "\n")
    
    messages.success(request, "File downloaded successfully!")
    return redirect("/showjobpost")



#show job post 
def showjobpost(request):
    company = jobpost.objects.all()
    if request.method=="GET":
        pm=request.GET.get('education_level')
        cm=request.GET.get('jobtitle')
        if pm!=None:
            company = jobpost.objects.filter(education_level=pm)
        if cm!=None:
            company = jobpost.objects.filter(job_title=cm)
            
          

    p = Paginator(company, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj} 
    return render(request,'job_post.html',context)

# show home page
def showjob1(request):
    productpage = jobpost.objects.all()
    if request.method=="GET" :
        us=request.GET.get('job_title')
        if us!=None:
            productpage = jobpost.objects.filter(job_title=us)


    p = Paginator(productpage, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj} 
    return render(request,'job.html',context)


#show job user side

def showjob(request):
    productpage = jobpost.objects.all()
    if request.method=="GET" :
        us=request.GET.get('job_title')
        if us!=None:
            productpage = jobpost.objects.filter(job_title=us)
    p = Paginator(productpage, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj} 
    return render(request,'job_user.html',context)

# job post delete admin side

def deletejobpost(request,job_id):
    context = {}
    obj = get_object_or_404(jobpost,job_id=job_id)
    if request.method == "GET":
        
        obj.delete()
        return redirect("/showjobpost")
    return render(request, "jobpost.html", context) 

    # change password company

def company_change_pswd(request):
    return render(request,'company_change_pswd.html')

def change_password(request):
    if request.method == "POST":    
        old_pswd = request.POST.get("password")
        username1 = request.POST.get("username1")
    
        obj = get_object_or_404(Company, username = username1)
        
        result = check_password(old_pswd, obj.password)
        # if obj.companyname == 2 and result == True:
        if result == True:
        
            new_pswd = request.POST.get("new_password")
            cnfm_pswd = request.POST.get("cnfm_password")
            
            if new_pswd == cnfm_pswd:
                
                obj.password = make_password(new_pswd)
                obj.save()
                
                messages.success(request, "Password Changed successfully!")
                return render(request,'companyprofile.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'company_change_pswd.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'company_change_pswd.html')
        


