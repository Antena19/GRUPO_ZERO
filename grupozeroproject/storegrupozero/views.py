from django.shortcuts import render
from .models import Technique, Product, Artist

def index(request):
    return render(request, 'index.html')

def artistas(request):
    artists = Artist.objects.all()
    return render(request, 'artistas.html', {'artists': artists})

def tecnicas(request):
    techniques = Technique.objects.all()
    return render(request, 'tecnicas.html', {'techniques': techniques})

def productos(request):
    products = Product.objects.all()
    return render(request, 'productos.html', {'products': products})

def login_view(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

