
from django.contrib import admin
from django.urls import path, include
from accounts import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', v.signup, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
