from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart),
    path('/remove', views.remove_from_cart)
]
