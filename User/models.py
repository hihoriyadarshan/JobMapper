from django.db import models
from Company.models import jobpost


# Create your models here.

class JobApplication(models.Model):
    
    job_id = models.ForeignKey(jobpost, on_delete=models.CASCADE)
    jobapplication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank = True,max_length=255,unique=True) 
    phone = models.CharField(max_length = 10,unique=True)
    resume = models.FileField(upload_to='media')
    status = models.CharField(max_length=20, default='Draft')   
    applied_at = models.DateTimeField(auto_now_add=True)

   