from django.shortcuts import render
from djangoProject.models import Article


def home(request):
    article = Article.objects.get(idarticle=7)
    context = {
        "object": article
    }
    return render(request, 'admin/admin.html', context)
