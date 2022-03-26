from decimal import Decimal

from django.conf import settings
from product.models import Article


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add_to_cart(self, product, quantity=1, override_quantity=False):
        print("dedanss")
        product_id = str(product.idarticle)
        if product_id not in self.cart:
            print("dans le if")
            self.cart[product_id] = {'quantity': 0, 'price': product.prix}
        else:
            new_quantity = self.cart[product_id]['quantity'] + quantity
            price = self.cart[product_id]['price'] * new_quantity
            self.cart[product_id] = {'quantity': new_quantity, 'price': price}

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
        product_ids = self.cart.keys()
        products = Article.objects.filter(idarticle=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.idarticle)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
