# storegrupozero/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('tecnicas/', views.tecnicas, name='tecnicas'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:product_id>/', views.producto_detalle, name='producto_detalle'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
