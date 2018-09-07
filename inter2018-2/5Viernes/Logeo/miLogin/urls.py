from django.urls import path
from . import views
from miLogin.views import VistaLogin, VistaInicio, VistaRegistro, VistaCerrar

urlpatterns = [
	path('', VistaLogin.as_view(),),
	path('inicio/', VistaInicio.as_view(), name = 'index'),
	path('login/', VistaLogin.as_view(), name='login'),
	path('registro/', VistaRegistro.as_view(), name='registro'),
	path('login/cerrar', VistaCerrar.as_view(), name='cerrar'),
]