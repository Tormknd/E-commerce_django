from datetime import datetime
from io import StringIO
from django.shortcuts import render

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
    return render(request, 'search.html', {'list': Article.objects.filter(nom__icontains=request.POST['chercher'])})


def categories(request):
    Categorie.objects.filter(idcategorie=request.GET.get('id', ''))
    r = Ranger.objects.filter(idcategorie=request.GET.get('id', ''))
    for x in r:
        print(x)
    # Article.objects.filter(idarticle=r.)
    context = {
        'list': 2
    }
    pass
    return render(request, 'search.html', context)
