import string
from django import forms  
from Company.models import company_contact

class company_contactForm(forms.ModelForm):  
    class Meta:  
        model = company_contact
        fields = ('name','email','message',)