import datetime

from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from adminInterface.models import Commande, Client
from cart.cart import Cart
from cart.models import Posseder
from djangoProject.createsession import CreateSession
from product.models import Article, AuthUser

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


def buy_cart_articles(request):
    cart = Cart(request)
    context = {
        'items': cart,
        'total_price': cart.get_total_price(),
    }
    if request.user.is_authenticated:
        client = AuthUser.objects.get(id=request.user.id)
        c = Commande(prixcommande=cart.get_total_price(), articletotal=len(cart.cart.values()), datecommande=datetime.datetime.now(), idclient=client)
        c.save()
        for x in cart:
            p = Posseder(numcommande=c.numcommande, idarticle=x['product'])
            print("produit", x['product'])
            p.save()
            cart.remove(x['product'])
    else:
        context['connected'] = False
        return render(request, 'article/cart.html', context)

    return redirect('/cart')
