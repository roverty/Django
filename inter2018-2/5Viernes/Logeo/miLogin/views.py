from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib import messages, sessions
from .models import User

# Create your views here.

class VistaLogin(View):
	form_class = LoginForm
	template = 'Login.html'
	initial = {'key':'value'}

	def get(self, request):
		form = self.form_class(initial = self.initial)
		return render(request, self.template, {'form': form})

	def post(self, request, *args, **kwargs):
		USUARIO_LOGEADO = request.session.get('USUARIO_LOGEADO')
		if not USUARIO_LOGEADO:
			request.session['USUARIO_LOGEADO'] = ""
		form = self.form_class(request.POST)
		if(form.is_valid()):
			user = form.save(commit=False)
			user.username = form.cleaned_data.get('username')
			user.password = form.cleaned_data.get('password')
			try:
				usuario = User.objects.get(username=user.username)
				if (USUARIO_LOGEADO != ""):
					messages.info(request, 'Usuario ya esta logeado')
				elif (user.password != usuario.password1):
					messages.info(request, 'Informacion erronea')
				else:
					request.session['USUARIO_LOGEADO'] = user.username
					messages.info(request, 'Bienvenid@ ' + user.username)
					return render(request, 'Inicio.html', {})
			except User.DoesNotExist:
				messages.info(request, 'Infromación errónea')
				redirect('login')
			return render(request, self.template, {'form': form})
		else:
			form = LoginForm()
			return render(request, self.template, {'form': form})


class VistaInicio(View):
	template = 'Inicio.html'
	def get(self, request):
		return render(request, self.template)


class VistaRegistro(View):
	form_class = SignUpForm
	template = 'Registro.html'
	initial = {'key':'value'}

	def get(self, request):
		form = self.form_class(initial = self.initial)
		return render(request, self.template, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if(form.is_valid()):
			user = form.save(commit=False)
			user.username = form.cleaned_data.get('username')
			user.password1 = form.cleaned_data.get('password1')
			user.password2 = form.cleaned_data.get('password2')
			if(user.password1 != user.password2):
				messages.info(request, 'Contraseñas no concuerdan.')
				return render(request, self.template, {'form':form})
			else:
				user.save()
				return HttpResponseRedirect('login')
		return render(request, self.template, {'form':form})

class VistaCerrar(View):
	def get(self, request):
		request.session['USUARIO_LOGEADO'] = ""
		messages.info(request, 'Se ha cerrado la sesion')
		return redirect('login')

		