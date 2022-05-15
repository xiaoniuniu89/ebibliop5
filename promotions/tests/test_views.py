import datetime
from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse
from promotions.models import Subscriber, NewsLetter


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
)
class TestViewResponses(TestCase):
    """Tests for promotions views"""

    def setUp(self):
        """ set up test variables"""
        self.client = Client()
        self.user = User.objects.create(username='admin'),
        self.sub1 = Subscriber.objects.create(
            email='email1@mail.com',
            slug_end='8692a064-cc49-4a74-84d2-bd2b287dfe37'
        )
        self.news = NewsLetter.objects.create(
            user=User.objects.all()[0],
            message='test message',
        )

    def test_add_subscriber(self):
        """test add subscriber to newletter"""
        response = self.client.post(
            reverse('promotions:subscribe'),
            {
                'action': 'post',
                'email': 'email2@mail.com'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'msg': 'email subscribed!'})
        response = self.client.post(
            reverse('promotions:subscribe'),
            {
                'action': 'post',
                'email': 'email1@mail.com'
            },
            xhr=True
        )
        self.assertEqual(response.json(), {'msg': 'email already subscribed!'})

    def test_newletter(self):
        NewsLetter.objects.create(
            user=User.objects.all()[0],
            message='test two'
        )
        self.assertEqual(NewsLetter.objects.all().count(), 2)

    def test_str(self):
        """ test model __str__ """
        data = self.news
        self.assertEqual(
            str(data),
            f'newsletter from admin on {datetime.date.today()}'
        )
        data = self.sub1
        self.assertEqual(
            str(data),
            'email1@mail.com'
        )
