from django.contrib import admin
from . import settings
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls'),name='inicio'),
    path('biblioteca/',include('biblioteca.urls'),name='biblioteca'),
    path('login/', include('miLogin.urls'),name='login'),
]


### necesitamos esto para construir las url correspondientes a nuestras imagenes
if settings.DEBUG is True:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
