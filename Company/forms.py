import string
from django import forms  
from Company.models import company_contact, jobpost

class company_contactForm(forms.ModelForm):  
    class Meta:  
        model = company_contact
        fields = ('name','email','message',)

class jobpostForm(forms.ModelForm):  
    class Meta:  
        model = jobpost
        fields = ('job_title','company_location','salary','experience_required','skill_required','post_date','last_date','image','job_description',)