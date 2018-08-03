from django.shortcuts import render
from .forms import Login
from django.views import View
# Create your views here.


class VistaLogin(View):
	tipo_forma = Login
	templete = 'miLogin/Login.html'
	initial = {'key':'value'}

	def get(self, request):
		form = self.tipo_forma(initial = self.initial)
		return render(request, self.templete, {'form':form})

	def post(self, request):
		form = self.tipo_forma(request.POST)
		if(form.is_valid()):
			return render(request, self.templete, {'form':form})
