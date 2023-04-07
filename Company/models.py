from django.db import models

# Create your models here.
class company_contact(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)

    
    def __str__(self):
        return self.name 
    
class jobpost(models.Model):

    # comapnyname = models.TextField(max_length = 50)
    job_title = models.TextField(max_length = 30)
    company_location = models.TextField(max_length = 50)
    salary = models.TextField(max_length = 50)
    experience_required = models.TextField(max_length = 50)
    # email = models.EmailField(blank = True,max_length=50)
    skill_required = models.CharField(max_length=20, null = True,blank=True)
    post_date = models.DateField(max_length = 15, null = True,blank=True)
    last_date = models.DateField(max_length = 15, null = True,blank=True)
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    job_description = models.TextField(max_length = 50)
    # terms_and_conditions = models.CharField(max_length=20)

    def __str__(self):
        return self.job_title