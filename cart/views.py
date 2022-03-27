from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from cart.cart import Cart
from djangoProject.createsession import CreateSession
from product.models import Article


def cart(request):
    CreateSession.session(CreateSession(), request)
    session_cart = Cart(request)
    print(session_cart.cart)
    # POUR TROUVER LE NOM DE L'ARTICLE
    keys = list(session_cart.cart.keys())
    for key in range(len(keys)):
        keys[key] = int(keys[key])
    my_filter = Q()
    for idarticle in keys:
        my_filter = my_filter | Q(idarticle=idarticle)
    item = Article.objects.filter(my_filter)
    item_list = item.values_list()
    # FIN
    # POUR TROUVER LA QUANTITÉ ET LE PRIX
    # final_dict = {}
    # for item in item_list:
    #     print(item[1])
    #     for x in session_cart:
    #         print(x)
    #     # final_dict[item[1]] = {'quantité': }

    # print(final_dict)
    context = {
        'items': session_cart,
        'total_price': session_cart.get_total_price()
    }
    return render(request, 'article/cart.html', context)
