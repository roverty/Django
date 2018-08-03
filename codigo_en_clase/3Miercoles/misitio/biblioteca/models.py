from django.db import models

# Create your models here.
#ORM
class Editor(models.Model):
	"""docstring for Editor"""
	nombre =models.CharField(max_length=30)
	domicilio =models.CharField(max_length=50)
	ciudad =models.CharField(max_length=30)
	estado =models.CharField(max_length=30)
	pais =models.CharField(max_length=30)
	sitioweb = models.URLField()

	def __str__(self):
		return self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	email = models.EmailField()
	def __str__(self):
		return '%s %s' %(self.nombre,self.apellidos)	

class Libro(models.Model):
	"""docstring for Libro"""
	titulo = models.CharField(max_length=50)
	autores = models.ManyToManyField(Autor)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
	fecha_publicacion = models.DateField()
	imagen = models.ImageField(upload_to='biblioteca/static')
	
	def __str__(self):
		return self.titulo	
		