from django.db import models

# Create your models here.
class SignUp(models.Model):
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    username = models.TextField(max_length = 255)
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
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    username = models.TextField(max_length = 45,unique=True)   
    email = models.EmailField(blank = True,max_length=255,unique=True) 
    phone = models.TextField(max_length = 10)  
    password = models.TextField(max_length = 255)  
         
    def __str__(self):
        return self.username 
		

#Comapny model

class Company(models.Model):
    username = models.TextField(max_length = 50) 
    companyname = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 10)
    email = models.EmailField(blank = True,max_length=50,unique=True) 
    password = models.TextField(max_length = 50)
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    # location = models.TextField(max_length = 250)
    # company_status=models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.username
    


#contact us model
class contact(models.Model):
    
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    