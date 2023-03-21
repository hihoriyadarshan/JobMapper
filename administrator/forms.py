import string
from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from administrator.models import blog

#blog
class blogForm(forms.ModelForm):  
    class Meta:  
        model = blog 
        fields = ('image','title','message',) 