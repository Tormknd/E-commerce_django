from datetime import datetime
from django.shortcuts import render
from product.models import Article
from adminInterface.json_datetime_serializer import JSONDateTimeSerializer
from .createsession import CreateSession


def home(request):
    CreateSession.session(CreateSession, request)
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



