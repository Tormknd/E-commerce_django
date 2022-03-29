import datetime

from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from adminInterface.views import check_client_device
from djangoProject.createsession import CreateSession
from .models import Article, Commenter, Commentaire, AuthUser
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
    if request.user.is_authenticated:
        connected = True
    else:
        connected = False
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    commentaires = comments(request)
    context = {
        "object": article,
        "comments": commentaires,
        'connected': connected
    }
    return render(request, 'article/article.html', context)


def add_item_to_cart(request):
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    product = "product=" + str(article.idarticle)
    cart = Cart(request)
    cart.add_to_cart(product=article, quantity=1, override_quantity=False)
    return redirect('/article/article.html?' + product)


def buy_one_item(request):
    global context
    global article
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    product = "product=" + str(article.idarticle)
    authuser = AuthUser.objects.get(id=request.user.id)
    item = Commande(prixcommande=article.prix, articletotal=1, datecommande=datetime.datetime.now(), idclient=authuser)
    item.save()
    article.nbventes = article.nbventes + 1
    article.save()
    return redirect('/article/article.html?' + product)


def comments(request):
    product_id = request.GET.get('product', '')
    comments_infos = Commenter.objects.filter(idarticle=product_id)
    final_comments = {}
    for x in comments_infos.values():
        c = Commentaire.objects.filter(idcommentaire=x['idcommentaire'])
        final_comments[x['idcommentaire']] = {
            'username': AuthUser.objects.filter(id=c.values()[0]['idclient']).values()[0]['username'],
            'text': c.values()[0]['textecommentaire'],
            'date': c.values()[0]['datecommentaire'],
            'client_id': c.values()[0]['idclient']
        }
    return final_comments


def add_comment(request):
    id_product = request.GET.get('product', '')
    x = request.POST.items()
    msg = ""
    for key, value in x:
        if key == 'msg':
            msg = value
    if request.user.id:
        c = Commentaire(idclient=request.user.id, textecommentaire=msg, datecommentaire=datetime.datetime.now())
        c.save()
        z = Commenter(idarticle=id_product, idclient=request.user.id, idcommentaire=c.idcommentaire)
        z.save()

    global article
    article = Article.objects.get(idarticle=id_product)
    product = "product=" + str(article.idarticle)
    return redirect('/article/article.html?' + product)
