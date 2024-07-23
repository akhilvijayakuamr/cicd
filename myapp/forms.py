
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Create Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":'form-control','placeholder':'Enter Your Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Your Password'}))
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']