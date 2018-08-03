from django.urls import path
from . import views
from miLogin.views import VistaLogin

urlpatterns = [
	path('', VistaLogin.as_view()),
]