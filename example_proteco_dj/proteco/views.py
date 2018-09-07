from django.http import HttpResponse 
from django.shortcuts import render
from django.views.generic import TemplateView
 
def inicio(request): 
    #return HttpResponse("Hola Mundo") 
    return render(request,'index.html')

class About(TemplateView):
	"""docstring for About"""
	template_name="about.html"	