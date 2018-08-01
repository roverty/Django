# Django

## Instalación en Ubuntu 16.04

### Instalar python

`apt install python3`

### Instalar django y pip

`apt install python3-django python3-pip`

### Instalar django con pip

`pip install django`

### Comprobar instalación

`python3 -m django --version`

## Mi primer sitio web

### Crear el projecto

`django-admin startproject <pjname>`

### Permitir ver servidor django en la red local

Modificar settings.py y agregar la siguiente linea

`ALLOWED_HOSTS = ['198.211.99.20', 'localhost', '127.0.0.1']`

### Correr el servidor

`python3 manage.py runserver`

`python3 manage.py runserver 8080`

`python3 manage.py runserver 192.168.1.73:8080`

## Bibliografía

https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04