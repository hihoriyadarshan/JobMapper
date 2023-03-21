from django.db import models

# Create your models here.

# blog

#blog  model 
class blog(models.Model):
    image = models.ImageField(upload_to = 'media', null = True,blank=True)
    title = models.TextField(max_length = 50)
    message = models.TextField(max_length = 501)
    blogdate = models.DateTimeField(auto_now=True)


