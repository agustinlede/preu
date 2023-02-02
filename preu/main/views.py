from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("HOLA")
    
# Create your views here.
