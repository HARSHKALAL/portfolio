from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class Userform(UserCreationForm):
    
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta: 
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    
class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']




