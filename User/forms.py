import string
from django import forms  
from User.models import JobApplication

class JobApplicationForm(forms.ModelForm):  
    class Meta:  
        model = JobApplication
        fields = ('name','email','phone','resume','status',)