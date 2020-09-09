from django.forms import ModelForm, forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'projects', 'start', 'end', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']

