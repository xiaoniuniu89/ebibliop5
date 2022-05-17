from django.contrib.auth.models import User
from django.test import Client, TransactionTestCase, override_settings
from django.urls import reverse
from dashboard.models import Profile

# for making product
small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
)
class TestViewResponses(TransactionTestCase):
    """Tests for store views"""

    def setUp(self):
        """ set up test variables"""
        self.client = Client()
        self.user = User.objects.create(username='bob')
        self.user.set_password('12345')
        self.user.save()
        self.profile = Profile.objects.get(user=self.user)
        self.client.login(username='bob', password='12345')

    def test_update_billing(self):
        response = self.client.post(
            reverse('dashboard:update_billing_info'),
            {
                'action': 'post',
                'firstName': 'test',
                'lastName': '',
                'address1': 'fake str',
                'address2': 'fake rd',
                'email': 'test@mail.com',
                'city': 'foo',
                'country': 'mars',
                'postCode': '123',
            },
            xhr=True

        )
        self.assertEqual(response.json(), {'msg': 'updated succesfully'})

    def test_profile_str(self):
        """ test profile __str__"""
        data = self.profile
        self.assertEqual(
            str(data),
            "bob's profile"
        )
