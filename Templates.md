# Django

[TOC]

## Templates (plantillas)

Una plantilla de Django es una cadena de texto destinada a separar la presentación de un documento de sus datos. Una plantilla define marcadores de posición y varios bits de lógica básica (etiquetas de plantilla) que regulan cómo se debe mostrar el documento. Por lo general, las plantillas se utilizan para producir HTML, pero las plantillas de Django son igualmente capaces de generar cualquier formato basado en texto.

### Archivos estáticos(HTML5,CSS3,JS) 

Los archivos estáticos incluyen cosas como CSS, JavaScript e imágenes que es posible que desee publicar junto con su sitio.

#### Configurar archivos estáticos

Abrimos `settings.py` y debemos agregar lo siguiente.

```python
# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

Ahora debemos crear un directorio con el nombre de `static` en el mismo lugar que `settings.py`

En la carpeta `static` vamos a crear dos directorios, uno con el nombre de `css` y otro con el nombre de `js`.

Dentro de cada directorio que creamos (css y js), vamos a crear un archivo main.css y main.js respectivamente.

#### Configurar templates

Creamos un directorio 

```python

```



os.path.join(BASE_DIR,'templates')

Variables

Filtros

Etiquetas de Django 

c. Método POST, DELETE 
c. Seguridad en formularios 

https://scotch.io/tutorials/working-with-django-templates-static-files

https://djangobook.com/django-templates/

https://www.tutorialspoint.com/django/django_template_system.htm