from django.shortcuts import render, redirect, get_object_or_404
from .models import Technique, Product, Artist, Cart, CartItem
from django.contrib.auth.decorators import login_required


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

def producto_detalle(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'producto_detalle.html', {'product': product})

def login_view(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    cart.items.add(cart_item)
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')
