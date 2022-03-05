from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def home(request):
    article_list = Article.objects.all()
    return render(request, 'accueil.html', {'article_list': article_list})


def test(request):
    article_list = Article.objects.all()
    if request.GET.get('module', '') == "onTest":
        return render(request, 'accueil.html', {'article_list': article_list})
    else:
        return 0


def articles(request):
    id = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id)
    context = {
        "object": article
    }
    return render(request, 'article/article.html', context)


