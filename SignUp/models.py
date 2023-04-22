from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    email = models.EmailField(blank = True,max_length=255,unique=True)
    skill = models.TextField(max_length = 45)
    phone = models.TextField(max_length = 10)
    gender = models.CharField(max_length=6)
    address = models.TextField(max_length = 255)
    password = models.TextField(max_length = 255)
    def __str__(self):
        return self.username
    

#admin login model
class Admin_Log(models.Model):
    username = models.CharField(max_length = 45,unique=True)   
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    email = models.EmailField(blank = True,max_length=255,unique=True) 
    phone = models.TextField(max_length = 10)  
    password = models.TextField(max_length = 255)  
    def __str__(self):
        return self.username 
		
#Comapny model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True) 
    companyname = models.CharField(max_length = 45,unique=True)
    email = models.EmailField(blank = True,max_length=255,unique=True) 
    phone = models.CharField(max_length = 10,unique=True)
    address =models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    password = models.CharField(max_length = 255)
    
    
#contact us model
class contact(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    