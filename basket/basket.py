from decimal import Decimal
from store.models import Product


class Basket():
    """
    A base Basket class to provide methods for the basket
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        promo = self.session.get('promo_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        if 'promo_key' not in request.session:
            promo = self.session['promo_key'] = 0
        self.basket = basket
        self.promo = promo

    def add(self, product):
        """Adding and updating product to basket"""
        product_id = str(product.id)

        # getting strange bug when using if product_id not in ....
        if product_id in self.basket:
            pass
        else:
            self.basket[product_id] = {'price': str(product.price)}

        self.save()

    def add_promo(self, promo):
        self.promo = self.session['promo_key'] = promo
        self.save()

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        """delete all contents in basket - remove from session"""
        del self.session['session_key']
        del self.session['promo_key']
        self.save()

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return len(self.basket)

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.basket.values())

    def get_discount(self):
        if self.promo:
            return round(
                (
                    self.promo / Decimal(100)
                ) * self.get_total_price(), 2)
        return Decimal(0)

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def save(self):
        self.session.modified = True
