from django.shortcuts import render
from biblioteca.models import Editor,Autor,Libro
# Create your views here.
def biblio(request):

	editores = Editor.objects.all()

	return render(request,'biblioteca/biblioteca.html',{'editors':editores})
