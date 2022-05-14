from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.test import Client, RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from store.models import Category, Product, Review
from store.views import landing
from django.urls import path
from importlib import import_module

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViewResponses(TestCase):
    """Tests for store views"""
    def setUp(self):
        """ set up test variables"""
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='admin')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='admin', password='12345')


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
                'basket_total': '5.00',
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'success': 'order created'})
    
