from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class AddTask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
