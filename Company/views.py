from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Company.forms import company_contactForm,jobpostForm
from Company.models import company_contact,jobpost
from django.core.paginator import Paginator
from SignUp.models import Company



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
        image = image
        )
      
        # data = jobpost.objects.all()
        # request.session['job_title'] = data.job_title

    
    return render (request, "jobpost.html")


#show job post 
def showjobpost(request):
    company = jobpost.objects.all()
    if request.method=="GET" :
        cm=request.GET.get('jobsearch')
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