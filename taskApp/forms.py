
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

class DateInput(forms.DateInput):
    input_type= 'date'


class AddTask(forms.ModelForm):
    class Meta:
       model= Task 
       fields='__all__'
       widgets = {
           'date':DateInput()
       }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        widgets= {
            'date':DateInput()
        }

class Create_user_f(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=TextInput())
    password= forms.CharField(widget=PasswordInput())
