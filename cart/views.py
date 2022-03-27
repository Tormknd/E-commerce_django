from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from cart.cart import Cart
from djangoProject.createsession import CreateSession
from product.models import Article

context = {
    "object": ""
}


def cart(request):
    global context
    CreateSession.session(CreateSession(), request)
    session_cart = Cart(request)
    context = {
        'items': session_cart,
        'total_price': session_cart.get_total_price()
    }
    return render(request, 'article/cart.html', context)


def remove_from_cart(request):
    art_id = request.GET.get('product', '')
    Cart(request).remove(art_id)
    return redirect('/cart')
