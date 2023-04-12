from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from administrator.forms import blogForm, categoryForm
from administrator.models import blog, Catagory
from django.core.paginator import Paginator

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

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
        return render (request, "admin.html")
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


#show blog

def showbloger(request):
    
    context = { 'blog_data': blog.objects.all() }
    return render(request, "blogpage.html", {'context': context})

# show blog company

def showbloger_company(request):
    context = { 'blog_data': blog.objects.all() }
    return render(request, "blogpage_company.html", {'context': context})

 
 # category

def add_category(request):  
   
    if request.method == "POST": 
        
        form = categoryForm(request.POST or None) 
        
        if form.is_valid():
            
            try:  
                form.save()  
                return render(request,'category.html')  
            except:  
                pass  
    else:  
        form = categoryForm()  
    return render(request,'category.html',{'form':form})


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


