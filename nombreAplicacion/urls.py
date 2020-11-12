from django.urls import path
from . import views
urlpatterns = [ 
	path('inicio', views.inicio, name='inicio'),
	path('deck', views.deck, name='deck'),
	path('admin', views.admin, name='admin'),
	path('login', views.login, name='login'),
	path('loginadmin', views.loginadmin, name='loginadmin'),
	path('registro', views.registro, name='Registro'),
	path('trucks', views.trucks, name='Trucks'),
]
