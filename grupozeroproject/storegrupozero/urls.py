# storegrupozero/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista principal
    path('artistas/', views.artistas, name='artistas'),
    path('tecnicas/', views.tecnicas, name='tecnicas'),
    path('productos/', views.productos, name='productos'),
    path('login/', views.login_view, name='login'),
]
