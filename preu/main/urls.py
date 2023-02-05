from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tareas/', views.tareas, name="tareas"),
    path('home/', views.home, name="home"),
    path('ensayos/', views.ensayos, name="ensayos"),
    path('calendario/', views.calendario, name="calendario"),
    

    
]
