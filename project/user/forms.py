from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('full_name', 'phone', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Email or Phone', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)