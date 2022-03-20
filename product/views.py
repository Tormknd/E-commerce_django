import datetime

from django.shortcuts import render
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
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    # mixins.send_article_signals(article, request)
    context = {
        "object": article
    }
    return render(request, 'article/article.html', context)


def buy_item(request):
    global context
    global article
    client = Client.objects.get(idclient=5)
    c = Commande(prixcommande=article.prix, articletotal=1, datecommande=datetime.datetime.now(), idclient=client)
    c.save()
    return render(request, 'article/article.html', context)

