# storegrupozero/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def artistas(request):
    return render(request, 'artistas.html')

def tecnicas(request):
    return render(request, 'tecnicas.html')

def productos(request):
    return render(request, 'productos.html')

def login_view(request):
    return render(request, 'login.html')
