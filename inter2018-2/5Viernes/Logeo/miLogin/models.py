from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario', primary_key=True)
    password1 = models.CharField(max_length=30, help_text='Contraseña')
    password2 = models.CharField(max_length=30, help_text='Confirmacion de contraseña')
    first_name = models.CharField(max_length=30, help_text='Nombre')
    last_name = models.CharField(max_length=30, help_text='Apellido')
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.username


class Logeo(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    password = models.CharField(max_length=30, help_text='Contraseña')

    def __str__(self):
        return self.username