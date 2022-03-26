import datetime

from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from adminInterface.views import check_client_device
from djangoProject.createsession import CreateSession
from .models import Article
from django.conf import settings
from adminInterface import mixins
from adminInterface.models import Commande, Client

# Create your views here.

User = settings.AUTH_USER_MODEL

context = {
    "object": ""
}

article = Article.objects.get(idarticle=3)


def articles(request):
    mixins.send_on_page_signals(request)
    CreateSession.session(CreateSession, request)
    check_client_device(request)
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    print(article.idarticle)
    # mixins.send_article_signals(article, request)
    context = {
        "object": article
    }
    return render(request, 'article/article.html', context)


def add_item_to_cart(request):
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    print(article.nom)
    product = "product=" + str(article.idarticle)
    cart = Cart(request)
    cart.add_to_cart(product=article, quantity=1, override_quantity=True)
    return redirect('/article/article.html?' + product)


def buy_item(request):
    global context
    global article
    product = "product=" + str(article.idarticle)
    print(product)
    client = Client.objects.get(idclient=5)
    c = Commande(prixcommande=article.prix, articletotal=1, datecommande=datetime.datetime.now(), idclient=client)
    c.save()
    return redirect('article.html?' + product)


