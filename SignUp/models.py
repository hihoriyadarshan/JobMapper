from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    password = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 10)

    def __str__(self):
        return self.username
    

#admin login model
class Admin_Log(models.Model):
    username = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50) 
    phone = models.TextField(max_length = 10)
      
    def __str__(self):
        return self.username 
		

#Comapny model

class Company(models.Model):
    username = models.TextField(max_length = 50) 
    companyname = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 10)
    email = models.EmailField(blank = True,max_length=50) 
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