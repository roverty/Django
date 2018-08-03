from django.shortcuts import render
from biblioteca.models import Editor,Autor,Libro
# Create your views here.
def biblio(request):

	editores = Editor.objects.all()
	libro = Libro.objects.all()

	return render(request,'biblioteca/biblioteca.html',{'editors':editores,'libros':libro})
def cards(request):
	libro = Libro.objects.all()	
	return render(request,'biblioteca/cartas.html',{'libros':libro})