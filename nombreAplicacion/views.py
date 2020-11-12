from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
def inicio(request):
	return render(request, 'inicio.html', {})

def deck(request):
    	return render(request, 'deck.html',{})

def admin(request):
    	return render(request,'admin.html',{})

def login(request):
    	return render(request,'login.html',{})

def loginadmin(request):
    	return render(request,'loginadmin.html',{})

def registro(request):
	
	if request.method == "POST":
		nombre	= request.POST["txtNombre"]
		correo	= request.POST["txtCorreo"]
		clave	= request.POST["txtClave"]
		User.objects.create(username=nombre, email=correo, password=make_password(clave))
		
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	return render(request, 'registro.html', {})	

def trucks(request):
	return render(request,'trucks.html',{})	