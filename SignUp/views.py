from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from SignUp.forms import SignUpForm, AdminForm, contactForm, companyForm
from SignUp.models import SignUp, Admin_Log, Company, contact
from Company.models import jobpost,company_contact
from administrator.models import blog
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib import messages
from administrator.models import Catagory 
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
# password hasing
from django.contrib.auth.hashers import make_password ,check_password
#loger
import logging,traceback
logger = logging.getLogger('authLogger')



# Create your views here.
def homepage(request):
    return render(request,"index.html")

def home_page(request):
    return render(request,"index.html")

def sign_up(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'registration.html')

def logout(request):
    return render(request,'index.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def companylogin(request):
    return render(request,'companylogin.html') 

def company(request):
    return render(request,'companyregistration.html') 

def companyhomepage(request):
    return render(request,'companyhomepage.html') 

def user(request):
          return render(request,'user.html')

def company_data(request):
          return render(request,'company.html')

def feedback(request):
        return render(request,'feedback.html')

def showcompanyprofile(request):
        return render(request,'showcompanyprofile.html')

def updateuser(request):
        return render(request,'update_user.html')

def updatecomapny(request):
        return render(request,'update_company.html')

def admin_signup(request):
    return render(request,'admin_signup.html')

def job1(request):
    return render(request,'job.html')


        
#user Registration
def sup(request):  
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


        # return HttpResponse(s.username)
        return render (request, "login.html")
    
    return HttpResponse('Fail')





def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(6) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.GET.get("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)

#user login
   
def loginHandle(request):
    
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")

        obj = get_object_or_404(SignUp, username = un )
        
        result = check_password(ps,obj.password)

        data = SignUp.objects.all()
        # return HttpResponse(form)
        for i in range(len(data)):
            if data[i].username == un:
                request.session['username'] = data[i].username
                request.session['email'] = data[i].email
                request.session['skill'] = data[i].skill
                request.session['phone'] = data[i].phone
                request.session['gender'] = data[i].gender
                request.session['address'] = data[i].address

        if result == True:

            logger.info("user: " + data[i].username + " is logged in")
            user_info = { 'username':data, 'email':data, 'skill':data, 'gender':data, 'phone':data, 'address':data}
            return render(request,'user-hp.html', {"user_info" :user_info}) 
        else :
            return render(request,'login.html')
        
    else:
        form = SignUpForm()
        return render(request, template_name = "login.html", context = {"form":form})
    

   
   
# user_data update 

def edituser(request, id):  
    context = {}
    obj = get_object_or_404(SignUp, id=id)
    form = SignUpForm(request.POST,request.FILES, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("/user") 
    return render(request, "user.html", context)


def updateuser(request,id):
    context = SignUp.objects.get(id=id)
    return render(request, "update_user.html",{'context' : context})


#delete user

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(SignUp,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showuser")
    return render(request, "user.html", context)
     

#show user

def showuser(request):
    users = SignUp.objects.all()
    user_count = SignUp.objects.all().count()
    if request.method=="GET" :
        us=request.GET.get('usersearch')
        if us!=None:
            users = SignUp.objects.filter(username=us)
    
    p = Paginator(users, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj,
              'user_count': user_count} 
    return render(request,'user.html',context)


#show userprofile
def showprofile(request):
    context ={"user_data":SignUp.objects.all()}
    return render(request, "userprofile.html", context)
    print('user_data')


#user_data pdf download
def user_pdf_report(request):
    users = SignUp.objects.all()
    template_path = 'pdf_report.html'
    context = {'users': users}
    # return HttpResponse(context['users'])
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="user_data.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # return HttpResponse(html)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# user_data csv download
def user_datacsvdownload(request):
    
    file_open = open("user_data.csv", "a")

    for user in SignUp.objects.all():
        file_open.write(str(user.id)+ "," +str(user.username)+ "," +str(user.email)+ "," +str(user.gender)
 + "," +str(user.skill)+ "," +str(user.phone)+ "\n")
    
    messages.success(request, "File downloaded successfully!")
    return render(request, "user.html")

 

# company registration
def company_data(request):  
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
        return render (request, "companylogin.html")
    return HttpResponse('Fail')

#company login
def loginHandlecompany(request):
    
    if request.method == "POST":    
        form = companyForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")

        obj = get_object_or_404(Company, username = un )
        
        result = check_password(ps,obj.password)

        data = Company.objects.all()

        for i in range(len(data)):
            if data[i].username == un:
                request.session['company_id'] = data[i].company_id
                request.session['companyname'] = data[i].companyname
                request.session['username'] = data[i].username
                request.session['email'] = data[i].email
                request.session['phone'] = data[i].phone
                request.session['address'] = data[i].address
            
        if result == True:

            logger.info("user: " + data[i].companyname + " is logged in")
            user_info = { 'company_id':data, 'companyname':data, 'username':data, 'email':data, 'phone':data, 'address':data}
            return render(request,'companyhomepage.html', {"user_info" :user_info})   
            #return HttpResponse(form)
        else :
            # return render(request,'userhomepage.html')
            return render(request,'companylogin.html')
       

    else:
        form = companyForm()
        return render(request, template_name = "companylogin.html", context = {"form":form})

# company bulk upload  
def bulk_upload(request):
    if request.method == 'GET':
        return render(request, "bulkUpload.html")
    
    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        return HttpResponse("File not valid")
    if csv_file.multiple_chunks():
        return HttpResponse("Uploaded file is big")
    
    file_data = csv_file.read().decode("UTF-8")
    lines = file_data.split("\n")
    c = len(lines)
    for i in range(0, c-1):
        fields = lines[i].split(",")
        data_dict = {}
        data_dict["username"] = fields[0]
        data_dict["companyname"] = fields[1]
        data_dict["phone"] = fields[2]
        data_dict["email"] = fields[3]
        data_dict["address"] = fields[4]
        # data_dict["image"] = fields[1]
        # data_dict["password"] = fields[1]


        
        form = companyForm(data_dict)
        if form.is_valid():
            form.save()
    
    return redirect("/showcompany")


# delete company data

def deletecompany(request,company_id):
    context = {}
    obj = get_object_or_404(Company,company_id=company_id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showcompany")
    return render(request, "company.html", context) 

#show company user    
def showcompany(request):
    company = Company.objects.all()
    if request.method=="GET" :
        us=request.GET.get('companysearch')
        if us!=None:
            company = Company.objects.filter(companyname=us)


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
    return render(request,'company.html',context)


#company data_update
def editcompany(request, company_id):  
    context = {}
    obj = get_object_or_404(Company, company_id=company_id)
    form = companyForm(request.POST,request.FILES, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("/showcompany") 
    return render(request, "company.html", context)


def updatecompany(request,company_id):
    context = Company.objects.get(company_id=company_id)
    return render(request, "update_company.html",{'context' : context})


 #show company profile

def showcompanyprofile(request):
    context ={"company_data":Company.objects.all()}
    return render(request, "companyprofile.html", context)
    print('company_data')

#company_data pdf download
def company_pdf_report(request):
    company = Company.objects.all()
    template_path = 'company_reportpdf.html'
    context = {'company': company}
    # return HttpResponse(context['users'])
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="company_data.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # return HttpResponse(html)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# user_data csv download
def company_datacsvdownload(request):
    
    file_open = open("company_data.csv", "a")

    for company in Company.objects.all():
        file_open.write(str(company.company_id)+ "," +str(company.username)+ "," +str(company.companyname)+ "," +str(company.email)+ "," +str(company.phone)
 +  "\n")
    
    messages.success(request, "File downloaded successfully!")
    return render(request, "company.html")




#Sub admin-add  

def admin_data(request):  
    if request.method == "POST": 
        a = Admin_Log()
        a.username = request.POST.get('username')
        a.phone = request.POST.get('phone')
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')
        a.password = make_password(a.password)
        
        a.save()
        return render (request, "admin.html")
    return HttpResponse('Fail')


#admin login

def loginHandleAdmin(request):
    
    if request.method == "POST":    
        form = AdminForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = Admin_Log.objects.all().filter(username=un)

        obj = get_object_or_404(Admin_Log, username = un )
        
        result = check_password(ps,obj.password)

        data = Admin_Log.objects.all()
        

        for i in range(len(data)):
            if data[i].username == un:
                request.session['username'] = data[i].username
                request.session['email'] = data[i].email
                request.session['phone'] = data[i].phone

        if result == True:            

            return render(request,'admin.html')
        else :
            return render(request,'adminlogin.html')
       
    else:
        form = AdminForm()
        return render(request, template_name = "index.html", context = {"form":form})
    

# show admin dashboard

def showadmindashboard(request):
    users = SignUp.objects.all()
    user_count = SignUp.objects.all().count()
    Company_count = Company.objects.all().count()
    job_post = jobpost.objects.all().count()
    category_count = Catagory.objects.all().count()
    company_feedback = company_contact.objects.all().count()
    feedback_count = contact.objects.all().count()
    blog_count = blog.objects.all().count()


   
    context ={'user_count': user_count,
              'company_count': Company_count, 
              'category_count': category_count,
              'job_post': job_post,
              'company_feedback': company_feedback,
              'feedback_count' : feedback_count,
              'blog_count' : blog_count
              
              } 
    return render(request,'admin.html',context)

# Contact us

def cont(request):  
   
    if request.method == "POST": 
        
        form = contactForm(request.POST or None) 
        
        if form.is_valid():
            
            try:  
                form.save()  
                return render(request,'home.html')  
            except:  
                pass  
    else:  
        form = contactForm()  
    return render(request,'index.html',{'form':form})



#show contact

def showcontact(request):
    contacts = contact.objects.all()
    p = Paginator(contacts, 10)
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
    return render(request,'feedback.html',context)
    

#delte feedback

def deletemessage(request,id):
    context = {}
    obj = get_object_or_404(contact,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showcontact")
    return render(request, "feedback.html", context)
   
      