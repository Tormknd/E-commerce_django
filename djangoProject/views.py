from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'accueil.html')


def test(request):
    if request.GET.get('module', '') == "onTest":
        return render(request, 'deaky.html')
    else:
        return render(request, 'base.html')

def dynamic(request, id):
    ret
