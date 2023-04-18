from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from SignUp.forms import SignUpForm, AdminForm, contactForm, companyForm
from SignUp.models import SignUp, Admin_Log, Company, contact
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib import messages
from administrator.models import Catagory 
# password hasing
from django.contrib.auth.hashers import make_password ,check_password



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



        
#user Registration
def sup(request):  
    if request.method == "POST": 
        s = SignUp()
        s.username = request.POST.get('username')
        s.email = request.POST.get('email')
        if SignUp.objects.filter(email=s.email).exists():
            #raise ValidationError("Email Exits")
            return render(request,"registration.html")
        s.job = request.POST.get('job')
        s.skill = request.POST.get('skill')
        s.hobbies = request.POST.get('hobbies')
        s.phone = request.POST.get('phone')
        s.address = request.POST.get('address')
        s.password = request.POST.get('password')

         # sup(request,un)
        # subject = 'welcome to JobMapper'
        # message = f'Hello, {s.username},Your registration has been confirmed for the JOb Mapper'
        # email_from = settings.EMAIL_HOST_USER
        # registration_list = [s.username, s.email]

        # send_mail( subject, message, email_from, registration_list)

        if len(request.FILES) != 0:
            s.image = request.FILES['image']
        #password Hashing
        # s.password = make_password(s.password)
        s.save()


        # return HttpResponse(s.username)
        return render (request, "login.html")
    
    return HttpResponse('Fail')

#user login
   
def loginHandle(request):
    
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        # if user.check_password(SignUp.password):

        

        uname = SignUp.objects.all().filter(username=un)
        
        if uname[0].username == un and uname[0].password == ps:
            # request.session['image'] = uname[0].FILES['image']
            request.session['username'] = uname[0].username
            request.session['email'] = uname[0].email
            request.session['job'] = uname[0].job
            request.session['hobbies'] = uname[0].hobbies
            request.session['skill'] = uname[0].skill
            request.session['phone'] = uname[0].phone
            request.session['address'] = uname[0].address
            

            # image =   len(request.FILES).session.image = request.FILES['image']            
            username = request.session['username']
            email = request.session['email']
            job = request.session['job']
            skill = request.session['skill']
            hobbies =request.session['hobbies']
            phone = request.session['phone']

            return render(request,'user-hp.html')
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
        file_open.write(str(user.id)+ "," +str(user.username)+ "," +str(user.email)+ "," +str(user.job)
 + "," +str(user.skill)+ "," + str(user.hobbies)+"," +str(user.phone)+ "\n")
    
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
        b.password = request.POST.get('password')

        if len(request.FILES) != 0:
            b.image = request.FILES['image']
        b.save()
        return render (request, "companylogin.html")
    return HttpResponse('Fail')

#company login
def loginHandlecompany(request):
    
    if request.method == "POST":    
        form = companyForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = Company.objects.all().filter(username=un)

        if uname[0].username == un and uname[0].password == ps:
            request.session['companyname'] = uname[0].companyname
            request.session['username'] = uname[0].username
            request.session['email'] = uname[0].email
            request.session['phone'] = uname[0].phone

            companyname = request.session['companyname']
            username = request.session['username']
            email = request.session['email']
            phone = request.session['phone']

            #return HttpResponse(form)
            return render(request,'companyhomepage.html')
        else :
            # return render(request,'userhomepage.html')
            return render(request,'companylogin.html')
       

    else:
        form = companyForm()
        return render(request, template_name = "companylogin.html", context = {"form":form})
    

# delete company data

def deletecompany(request,id):
    context = {}
    obj = get_object_or_404(Company,id=id)
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
def editcompany(request, id):  
    context = {}
    obj = get_object_or_404(Company, id=id)
    form = companyForm(request.POST,request.FILES, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("/showcompany") 
    return render(request, "company.html", context)


def updatecompany(request,id):
    context = Company.objects.get(id=id)
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
        file_open.write(str(company.id)+ "," +str(company.username)+ "," +str(company.companyname)+ "," +str(company.email)+ "," +str(company.phone)
 +  "\n")
    
    messages.success(request, "File downloaded successfully!")
    return render(request, "company.html")




#admin Signup

def admin_data(request):  
    if request.method == "POST": 
        a = Admin_Log()
        a.username = request.POST.get('username')
        a.phone = request.POST.get('phone')
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')

        
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
        

        if uname[0].username == un and uname[0].password == ps:
            request.session['username'] = uname[0].username
            request.session['email'] = uname[0].email
            request.session['phone'] = uname[0].phone

            username = request.session['username']
            email = request.session['email']
            phone = request.session['phone']
            

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
    category_count = Catagory.objects.all().count()

   
    context ={'user_count': user_count,
              'company_count': Company_count, 
              'category_count': category_count} 
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
   
      