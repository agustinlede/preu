from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, "main/home.html")

def tareas(response):
    return render(response, "main/tareas.html")
    
# Create your views here.
