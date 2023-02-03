from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tareas/', views.tareas),
    path('home/', views.home)
    
]
