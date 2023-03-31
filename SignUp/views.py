from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from SignUp.forms import SignUpForm, AdminForm, contactForm, companyForm
from SignUp.models import SignUp, Admin_Log, Company, contact
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
# from xhtml2pdf import pisa
# from django.template.loader import get_template

# pdf








# Create your views here.
def homepage(request):
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
        uname = SignUp.objects.all().filter(username=un)

        if uname[0].username == un and uname[0].password == ps:
            request.session['username'] = uname[0].username
            request.session['email'] = uname[0].email
            request.session['job'] = uname[0].job
            request.session['hobbies'] = uname[0].hobbies
            request.session['skill'] = uname[0].skill
            request.session['phone'] = uname[0].phone
            request.session['address'] = uname[0].address
            


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


#show user

def showuser(request):
    users = SignUp.objects.all()
    p = Paginator(users, 10)
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
    return render(request,'user.html',context)

#show company user
def showcompany(request):
    company = Company.objects.all()
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
    return render(request,'company.html',context)

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


# delete user data

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(SignUp,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showuser")
    return render(request, "user.html", context)

#delte blog

def deletemessage(request,id):
    context = {}
    obj = get_object_or_404(contact,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showcontact")
    return render(request, "feedback.html", context)


#show profile
def showprofile(request):
    context ={"user_data":SignUp.objects.all()}
    return render(request, "profile.html", context)
    print('user_data')


 #show company profile

def showcompanyprofile(request):
    context ={"company_data":Company.objects.all()}
    return render(request, "companyprofile.html", context)
    print('company_data')


#pdf download

# def pdf_company_report(request):
#     products = Company.objects.all()
#     template_path = 'pdf_company.html'

#     context = {'products': products}

#     response = HttpResponse(content_type='application/pdf')

#     response['Content-Disposition'] = 'filename="product_report.pdf"'

#     template = get_template(template_path)

#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html,dest=response)
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#        return response


      