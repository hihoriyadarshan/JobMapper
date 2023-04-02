from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Company.forms import company_contactForm
from Company.models import company_contact
from django.core.paginator import Paginator


def companyhomepage(request):
    return render(request,"companyhomepage.html")


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