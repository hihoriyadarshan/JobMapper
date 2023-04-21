import string
from django import forms  
from SignUp.models import SignUp,Admin_Log, contact, Company


class SignUpForm(forms.ModelForm):  
    class Meta:  
        model = SignUp  
        fields = ('image','username','email','skill','phone','gender','address','password',)

class AdminForm(forms.ModelForm):  
    class Meta:  
        model = Admin_Log  
        fields = ('image','username','password','email','phone',)

class contactForm(forms.ModelForm):  
    class Meta:  
        model = contact  
        fields = ('name','email','message',)

class companyForm(forms.ModelForm):  
    class Meta:  
        model = Company  
        fields = ('username','companyname','phone','email','address','image','password',)