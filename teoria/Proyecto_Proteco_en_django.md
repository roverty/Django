# Proyecto Proteco en django

## Iniciar proyecto

`django-admin startproject proteco`

## Recomendación de estructura de proyecto

```none
proteco_project
--media
--static
----css
----js
--templates
----partials
```

Y no olvidar crear `views.py`

## Iniciar aplicación

`python3 manage.py startapp cursos`

No olvide crear `views.py`

## Crear la siguiente jerarquía de directorios  y archivos en la aplicación

```none
cursos
--media
--templates
----base.html
----index.html
----partials
------navbar.html
------footer.html
--static
----css
------main.css
----js
------main.js
```

## Editar setting.py

```python
LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'
#############

ALLOWED_HOSTS = ['*']

############
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cursos',
]

############

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            os.path.join(BASE_DIR, 'cursos/templates')],##Templates de nuestras apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
                              
#############
                              
# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'cursos/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')                              

```

