from django.urls import path
from . import views

urlpatterns =[
	path('',views.biblio,name='biblioteca'),
	path('cartas',views.cards,name='cartas'),
]