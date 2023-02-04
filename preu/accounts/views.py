from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm   

def registerPage(response):
    form = CreateUserForm()

    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        



    context = {'form':form}
    return render(response, 'accounts/register.html', context)

def loginPage(response):
    context = {}
    return render(response, 'accounts/login.html', context)