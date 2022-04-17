

class Basket():
    """
    A base Basket class to provide methods for the basket
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def add(self, product):
        """Adding and updating product to basket"""
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price)}
        self.save()

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        print(self.basket)
        print(len(self.basket))
        return len(self.basket)

    def save(self):
        self.session.modified = True
