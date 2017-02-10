
from django import forms
from django.contrib.auth.models import User

from .models import Register



class UserForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['name', 'password', 'email','phone']



class LoginForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['name', 'password']
