from django.db import models

# Create your models here.
class SignUp(models.Model):
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    username = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50,unique=True)
    job = models.TextField(max_length = 50)
    skill = models.TextField(max_length = 50)
    hobbies = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 10)
    address = models.TextField(max_length = 500)
    password = models.TextField(max_length = 50)

    def __str__(self):
        return self.username
    

#admin login model
class Admin_Log(models.Model):
    username = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50) 
    phone = models.TextField(max_length = 10)
    hobbies = models.TextField(max_length = 50)
    address = models.TextField(max_length = 500)

      
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

    def __str__(self):
        return self.username
    



    





#contact us model
class contact(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)
    
    def __str__(self):
        return self.name 