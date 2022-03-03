from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'accueil.html')


def test(request):
    if request.GET.get('module', '') == "onTest":
        return render(request, 'accueil.html')
    else:
        return 0

def articles(request):
    return render(request, 'article/article.html')

