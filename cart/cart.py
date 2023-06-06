from decimal import Decimal
from django.conf import settings
from store.models import Product


class Cart(object):
    """
    class for cart(estate)
    """

    def __init__(self, request):
        """
        initialize bush
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save CLEAR bush in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Sorting through items in the basket and getting products from the database.
        """
        product_ids = self.cart.keys()
        # give ESTATE and added them into bush
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counts estates
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        added to the bush or restart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'cost': str(product.cost)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        save estate
        """
        self.session.modified = True

    def remove(self, product):
        """
        deleting estate
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """
        getting total price
        """
        print(self.cart.values())
        return sum(Decimal(item['cost']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        clear bush in session
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
