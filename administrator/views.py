from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from administrator.forms import blogForm
from administrator.models import blog
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

 