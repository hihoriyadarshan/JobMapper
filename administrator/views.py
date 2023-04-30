from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from administrator.forms import blogForm, categoryForm
from Company.forms import  jobpostForm
from administrator.models import blog, Catagory
from django.core.paginator import Paginator
from SignUp.models import SignUp,Company,Admin_Log
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password ,check_password
from django.contrib import messages
import logging,traceback
logger = logging.getLogger('authLogger')
import pandas as pd

# Create your views here.


# def blogpage(request):
#     return render(request,'admin.html')

def adminblog(request): 
    return render(request, "adminblog.html", {'blogs': blog.objects.all()})


def blogpage(request):
    return render(request,'blogpage.html')


def adminprofile(request):
    return render(request,'adminprofile.html')

def adminLTE(request):
    return render(request,'admin.html')

def writeblog(request):
    return render(request,'writeblog.html')



#blog
def bloger(request):  
    if request.method == "POST": 
        b = blog()
        b.title = request.POST.get('title')
        b.message = request.POST.get('message')
        b.blogdate = request.POST.get('blogdate')

        if len(request.FILES) != 0:
            b.image = request.FILES['image']
        b.save()

        #return HttpResponse(b)
        return render (request, "writeblog.html")
    return HttpResponse('Fail')


#Blog data_update
def editblog(request, id):  
    context = {}
    obj = get_object_or_404(blog, id=id)
    form = blogForm(request.POST,request.FILES, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("/adminblog") 
    return render(request, "adminblog.html", context)


def updateblog(request,id):
    context = blog.objects.get(id=id)
    return render(request, "update_blog.html",{'context' : context})


#delete blog
def deleteblog(request,id):
    context = {}
    obj = get_object_or_404(blog,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/adminblog")
    return render(request, "adminblog.html", context)


#show user blog

def showbloger(request):
    
    context = { 'blog_data': blog.objects.all() }
    return render(request, "blogpage.html", {'context': context})

# show blog company

def showbloger_company(request):
    context = { 'blog_data': blog.objects.all() }
    return render(request, "blogpage_company.html", {'context': context})


# show blog home

def showbloger_home(request):
    context = { 'blog_data': blog.objects.all() }
    return render(request, "homeblog.html", {'context': context})
 
 # category

def add_category(request):  
   
    if request.method == "POST": 
        
        form = categoryForm(request.POST or None) 
        
        if form.is_valid():
            
            try:  
                form.save()  
                return redirect(request,'/category')  
            except:  
                pass  
    else:  
        form = categoryForm()  
    return redirect("/category",{'form':form})
 

#Category update
def editadd_category(request, id):  
    context = {}
    obj = get_object_or_404(Catagory, id=id)
    form = categoryForm(request.POST,request.FILES, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("/category") 
    return render(request, "category.html", context)


def updatecompany(request,id):
    context = Catagory.objects.get(id=id)
    return render(request, "category.html",{'context' : context})



# show category

def category(request):
    category = Catagory.objects.all()
    # return HttpResponse(category)
    p = Paginator(category, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    # context ={'page_obj': page_obj} 
    return render(request,'category.html',  context ={'showcategory': page_obj} )


#delete Category

def deletecategory(request,id):
    context = {}
    obj = get_object_or_404(Catagory,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/category")
    return render(request, "category.html", context)

# change password user
def admin_change_pswd(request):
    return render(request,'admin_change_pswd.html')

def change_password2(request):
    if request.method == "POST":    
        old_pswd = request.POST.get("password")
        username1 = request.POST.get("username1")
    
        obj = get_object_or_404(Admin_Log, username = username1)
        
        result = check_password(old_pswd, obj.password)
        if result == True:
            new_pswd = request.POST.get("new_password")
            cnfm_pswd = request.POST.get("cnfm_password")
            
            if new_pswd == cnfm_pswd:
                
                obj.password = make_password(new_pswd)
                obj.save()
                
                messages.success(request, "Password Changed successfully!")
                return render(request,'admin_change_pswd.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'admin_change_pswd.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'admin_change_pswd.html')






# admin add User

#user Registration
def sup1(request):  
    if request.method == "POST": 
        s = SignUp()
        s.username = request.POST.get('username')
        s.email = request.POST.get('email')
        if SignUp.objects.filter(email=s.email).exists():
            #raise ValidationError("Email Exits")
            return render(request,"registration.html")
        s.skill = request.POST.get('skill')
        s.phone = request.POST.get('phone')
        s.gender = request.POST.get('gender')
        s.address = request.POST.get('address')
        s.password = request.POST.get('password')    

        if len(request.FILES) != 0:
            s.image = request.FILES['image']

        subject = 'welcome to JobMapper'
        message = f'Hello, {s.username},Your registration has been confirmed for the JOb Mapper'
        email_from = settings.EMAIL_HOST_USER
        registration_list = [s.username, s.email]

        #password Hashing
        s.password = make_password(s.password)



        send_mail( subject, message, email_from, registration_list)

        send_mail( subject, message, email_from, registration_list)
        s.save()

        users = SignUp.objects.all()

        # return HttpResponse(s.username)
        return redirect ("/showuser",{"context": users})
    
    return HttpResponse('Fail')


# Company add user
def company_data1(request):  
    if request.method == "POST": 
        b = Company()
        b.username = request.POST.get('username')
        b.companyname = request.POST.get('companyname')
        b.phone = request.POST.get('phone')
        b.email = request.POST.get('email')
        b.address = request.POST.get('address')
        b.password = request.POST.get('password')

        if len(request.FILES) != 0:
            b.image = request.FILES['image']

        subject = 'welcome to JobMapper'
        message = f'Hello, {b.username},Your Company has been registration Succesfully'
        email_from = settings.EMAIL_HOST_USER
        registration_list = [b.username, b.email]    

        b.password = make_password(b.password)

        send_mail( subject, message, email_from, registration_list)

        send_mail( subject, message, email_from, registration_list)

        b.save()
        return redirect("/showcompany")
    return HttpResponse('Fail')
