from django import forms
from .models import Logeado

class Login(forms.ModelForm):
	class Meta:
		model = Logeado;
		fields = ('usuario', 'contraseña')
		labels = {'usuario' : 'Nombre de Usuario',
			'contraseña' : 'Inserte su contraseña'}
		widgets = {
			'contraseña' : forms.PasswordInput(),
			}
