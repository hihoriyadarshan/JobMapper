from django.db import models
from SignUp.models import Company

# Create your models here.
class company_contact(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
    
class jobpost(models.Model):

    companyname = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_id = models.AutoField(primary_key=True)
    job_title = models.TextField(max_length = 45)
    salary = models.TextField(max_length = 10)
    experience_required = models.TextField(max_length = 10)
    jobtype = models.TextField(blank = True,max_length=45)
    skill_required = models.CharField(max_length=45, null = True,blank=True)
    education_level = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now=True)  
    last_date = models.CharField(max_length = 10, null = True,blank=True)
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    job_description = models.TextField(max_length = 255)
   
  