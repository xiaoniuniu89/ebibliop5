import datetime

from django.contrib.auth.models import User
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from store.models import Category, Product

from promotions.models import Promo

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
)
class TestBasketViews(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='test', slug='test')
        self.product = Product.objects.create(
            title='django for life',
            slug='django-for-life',
            price='10',
            image=SimpleUploadedFile(
                'small.gif',
                small_gif,
                content_type='image/gif'),
            pdf='django.pdf',
            author='admin',
            in_stock=True,
            description='book for test',
            rating_count=0,
            rating_score=0,
            category=Category.objects.all()[0])
        tz = timezone.get_current_timezone()
        self.promo = Promo.objects.create(
            code='DJANGO', valid_from=datetime.datetime.now().replace(
                tzinfo=tz), valid_to=datetime.datetime.now().replace(
                tzinfo=tz), discount=50, active=True)

    def test_basket_url(self):
        """ test baslet response """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add_duplicate(self):
        """ test adding items to basket - 1 from setup and 1 sent here"""
        self.client.post(
            reverse('basket:basket_add'),
            {
                'productId': self.product.id,
                'action': 'post'
            },
            xhr=True
        )
        # product id already in bag

        response = self.client.post(
            reverse('basket:basket_add'),
            {
                'productId': self.product.id,
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1})

    def test_basket_add(self):
        """ test adding items to basket """
        response = self.client.post(
            reverse('basket:basket_add'),
            {
                'productId': self.product.id,
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1})
        response = self.client.post(
            reverse('promotions:add_promo'),
            {
                'promo_code': 'DJANGO',
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(
            response.json(),
            {
                'code': 50,
                'discount': '5.00',
                'total': '5.00'
            }
        )

        def test_add_order_view(self):
            response = self.client.post(
                reverse('orders:add_order'),
                {
                    'order_key': '1234',
                    'name': 'John Doe',
                    'email': 'test@mail.com',
                    'address1': 'fake street',
                    'address2': 'fake rd',
                    'city': 'foo',
                    'country': 'mars',
                    'postcode': '123',
                    'promo': '5.00',
                    'basket_total': '5.00'
                }
            )

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
        self.assertEqual(response.json(), {'qty': 0, 'subtotal': '0'})

    def test_str(self):
        """ test model __str__ """
        data = self.promo
        self.assertEqual(
            str(data),
            'DJANGO'
        )
