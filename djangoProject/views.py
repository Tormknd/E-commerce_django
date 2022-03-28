from datetime import datetime
from io import StringIO
from django.shortcuts import render, redirect

from adminInterface.models import Categorie, Ranger
from adminInterface.views import check_client_device
from cart.cart import Cart
from product.models import Article
from adminInterface.json_datetime_serializer import JSONDateTimeSerializer
from .createsession import CreateSession
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import psycopg2


def home(request):
    CreateSession.session(CreateSession(), request)
    check_client_device(request)
    return render(request, 'accueil.html', {'article_list': Article.objects.all()})


def test(request):
    if request.GET.get('module', '') == "onTest":
        return render(request, 'accueil.html', {'article_list': Article.objects.all()})
    else:
        return 0


def about(request):
    if request.session.test_cookie_worked():
        print("the test cookie worked", request.session.get_session_cookie_age())
        request.session.delete_test_cookie()

    return render(request, 'accueil.html', {'article_list': Article.objects.all()})


def search(request):
    test = {
        'list': Article.objects.filter(nom__icontains=request.POST['chercher'])
    }
    print(test)
    return render(request, 'search.html', {'list': Article.objects.filter(nom__icontains=request.POST['chercher'])})


def categories(request):
    list = {}

    val = 0
    r = Ranger.objects.filter(idcategorie=request.GET.get('categorie', ''))
    article = [[0 for x in range(5)]for y in range(len(r))]
    for x in r.values():
        a = Article.objects.filter(idarticle=x['idarticle'])
        article[val][0] = a.values()[0]['idarticle']
        article[val][1] = a.values()[0]['nom']
        article[val][2] = a.values()[0]['url']
        article[val][3] = a.values()[0]['prix']

        val += 1
    list = {
        'list': article
    }
    print(list)

    return render(request, 'filter/categories.html', list)
