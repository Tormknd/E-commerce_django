from decimal import Decimal

from django.conf import settings
from django.db.models import Q

from product.models import Article


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add_to_cart(self, product, quantity=1, override_quantity=False):
        product_id = str(product.idarticle)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': product.prix}
        else:
            new_quantity = self.cart[product_id]['quantity'] + quantity
            # price = product.prix * new_quantity
            self.cart[product_id] = {'quantity': new_quantity, 'price': product.prix}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity

        self.save()
        print(self.cart)

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = product.idarticle
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = list(self.cart.keys())
        for key in range(len(product_ids)):
            product_ids[key] = int(product_ids[key])
        my_filter = Q()
        for idarticle in product_ids:
            my_filter = my_filter | Q(idarticle=idarticle)
        products = Article.objects.filter(my_filter)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.idarticle)]['product'] = product.nom
            cart[str(product.idarticle)]['url'] = product.url

        for item in cart.values():
            item['price'] = item['price']
            print(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
