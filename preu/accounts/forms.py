from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

cursos = (
    ('Primero Medio', 'Primero Medio'),
    ('Segundo Medio', 'Segundo Medio'),
    ('Tercero Medio', 'Tercero Medio'),
    ('Cuarto Medio', 'Cuarto Medio')
)

#class RegisterForm(UserCreationForm):
#    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class':'form-control'}))
#    first_name = forms.CharField(max_length=200)
#    last_name = forms.CharField(max_length=200)
#    curso = forms.ChoiceField(choices=cursos, widget=forms.Select(attrs={'class':'form-control'}))
#    
#    class Meta:
#        model = User
#        fields = ("first_name", 'last_name', 'curso',"email", "password1", "password2")
#        labels = {"email": "Email"}
