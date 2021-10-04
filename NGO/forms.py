from django import forms
from django.contrib.auth.models import User
from . import models

class NGOUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }

class NGOForm(forms.ModelForm):
    class Meta:
        model=models.NGO
        fields=['address','mobile','profile_pic']