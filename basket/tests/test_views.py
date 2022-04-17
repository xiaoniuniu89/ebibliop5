from django.contrib.auth.models import User
from django.http import HttpRequest

from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketViews(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='test', slug='test')
        Product.objects.create(
            category_id=1,
            title='test book',
            created_by_id=1,
            slug='test-book',
            price='9.99',
            image='test'
        )
        self.client.post(
            reverse('basket:basket_add'),
            {
                'productId': 1,
                'action': 'post'
            },
            xhr=True
        )

    def test_basket_url(self):
        """ test baslet response """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """ test adding items to basket - 1 from setup and 1 sent here"""
        response = self.client.post(
            reverse('basket:basket_add'),
            {
                'productId': 1,
                'action': 'post'
            },
            xhr=True
        )
        # one from setup and one from test = qty 2 
        self.assertEqual(response.json(), {'qty': 2})

    def test_basket_delete(self):
        """ test basket delete """
        response = self.client.post(
            reverse('basket:basket_delete'),
            {
                'productId': 1,
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'qty': 0, 'subtotal': 0})





