from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    firstName = forms.CharField(max_length="300")

    class Meta:
        model = User
        fields = ["firstName", "email", "password1", "password2"]

