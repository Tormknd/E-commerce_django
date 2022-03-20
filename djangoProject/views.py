from datetime import datetime
from io import StringIO
from django.shortcuts import render

from adminInterface.views import check_client_device
from product.models import Article
from adminInterface.json_datetime_serializer import JSONDateTimeSerializer
from .createsession import CreateSession
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import psycopg2


def home(request):
    CreateSession.session(CreateSession, request)
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



