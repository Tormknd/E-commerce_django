from django.shortcuts import render
from djangoProject.createsession import CreateSession
from .models import Article
from django.conf import settings
from adminInterface import mixins

# Create your views here.

User = settings.AUTH_USER_MODEL


def articles(request):
    CreateSession.session(CreateSession, request)
    id_product = request.GET.get('product', '')
    article = Article.objects.get(idarticle=id_product)
    mixins.send_article_signals(article, request)
    context = {
        "object": article
    }
    return render(request, 'article/article.html', context)
