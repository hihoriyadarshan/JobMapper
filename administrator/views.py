from django.shortcuts import render,redirect
from django.http import HttpResponse
from administrator.forms import blogForm
from administrator.models import blog
from django.core.paginator import Paginator

# Create your views here.


# def blogpage(request):
#     return render(request,'admin.html')

def adminblog(request):
    return render(request,'adminblog.html') 

def blogpage(request):
    return render(request,'blogpage.html')




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



#show blog

def showadminblog(request):
    context = { 'adminblog_data': blog.objects.all() }
    return render(request, "adminblog.html", {'context': context})


