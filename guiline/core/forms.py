from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your Username",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your Password",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your Username",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Your Email",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your Password",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Retype Password",
        "class": "w-full py-4 px-6 rounded-l"
    }))
    
