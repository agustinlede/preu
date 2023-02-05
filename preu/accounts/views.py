from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, f'Your account has been created. You can log in now')
        return redirect('login')
    else:
        form = RegisterForm()
    
    context = {'form':form}

    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)