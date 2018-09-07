from django import forms
from .models import User, Logeo

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        labels = {
            'username' : "Nombre de usuario",
            'first_name': "Nombre(s)",
            'last_name': "Apellido(s)",
            'email': "Correo electronico",
            'password1': "Contraseña",
            'password2': "Confirmacion de contraseña",
        }
        widgets = {
            'password2' : forms.PasswordInput(),
            'password1' : forms.PasswordInput(),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Logeo
        fields = ('username', 'password')
        labels = {
            'username': "Nombre de usuario",
            'password': "Contraseña",
        }
        widgets = {
            'password' : forms.PasswordInput()
        }