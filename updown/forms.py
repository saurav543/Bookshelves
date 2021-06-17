from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import book

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password1','password2')
    
class BookCreate(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'