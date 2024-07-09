# storegrupozero/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('tecnicas/', views.tecnicas, name='tecnicas'),
    path('productos/', views.productos, name='productos'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
]
