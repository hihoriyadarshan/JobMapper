from django.db import models

# Create your models here.
class company_contact(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    message = models.TextField(max_length = 300)

    
    def __str__(self):
        return self.name 