from django.shortcuts import render,redirect
from django.http import HttpResponse
from SignUp.forms import SignUpForm, AdminForm, contactForm, companyForm
from SignUp.models import SignUp, Admin_Log, Company
from django.core.paginator import Paginator


# Create your views here.
def homepage(request):
    return render(request,"index.html")


def sign_up(request):
    return render(request,'login.html')
    # return HttpResponse("hello");

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





#user  Registration
def signup(request):
    return render(request,'registration.html')

def sup(request):  
   
    if request.method == "POST": 
        
        form = SignUpForm(request.POST or None)  
            
        if form.is_valid():  
            try:  
                print("Hello")
                form.save()  
                return render(request,'registration.html')  
            except:  
                pass  
    else:  
        form = SignUpForm()  
    return render(request,'home.html',{'form':form})


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
            request.session['phone'] = uname[0].phone

            username = request.session['username']
            email = request.session['email']
            phone = request.session['phone']

            return render(request,'userhomepage.html')
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
            request.session['username'] = uname[0].username
            request.session['email'] = uname[0].email
            request.session['phone'] = uname[0].phone

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
def contact(request):  
   
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






# show user data

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



# delete user data

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(SignUp,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/showuser")
    return render(request, "user.html", context)