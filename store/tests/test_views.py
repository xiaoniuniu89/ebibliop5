from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.test import Client, RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import path

from store.models import Category, Product, Review

# for making product
small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


def response_error_handler(request, exception=None):
    """ for raising error exceptions """
    return HttpResponse('Error handler content', status=403)


def permission_denied_view(request):
    """ mock 403 response"""
    raise PermissionDenied


def bad_request_view(request):
    """ raise bad request"""
    raise SuspiciousOperation


urlpatterns = [
    path('403/', permission_denied_view),
    path('400/', bad_request_view),
]

handler400 = response_error_handler
handler403 = response_error_handler


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
)
class TestViewResponses(TestCase):
    """Tests for store views"""

    def setUp(self):
        """ set up test variables"""
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='admin')
        self.user.set_password('12345')
        self.user.save()
        Category.objects.create(name='django', slug='django')
        self.client.login(username='admin', password='12345')
        self.product = Product.objects.create(
            category_id=1,
            title='django beginners',
            slug='django-beginners',
            price='9.99',
            image=SimpleUploadedFile(
                'small.gif',
                small_gif,
                content_type='image/gif'),
            pdf='django',
            rating_count=0,
            rating_score=0)

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get('/', HTTP_HOST='e-biblio.herokuapp.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        """ test 404 response uses 404.html """
        self.client.get('/1234/4321')
        self.assertTemplateUsed('404.html')

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.client.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.client.get(
            reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)
        self.product.rating_count = 1
        self.product.rating_score = 5
        self.product.save()
        response = self.client.get(
            reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(
            reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_all_books(self):
        """
        test all books list page
        """
        response = self.client.get(
            reverse('store:all_books')
        )
        self.assertInHTML(
            '<title>Ebiblio | All Books</title>',
            response.content.decode()
        )

    def test_add_update_delete_review(self):
        """ tests ajax call to add, update and delete review"""
        response = self.client.post(
            reverse('store:handle_review'),
            {
                'product_id': 1,
                'rating': 3,
                'review': 'test review',
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(
            response.json(),
            {
                'msg': 'Post created',
                'rating': '3',
                'review': 'test review'
            }
        )
        self.assertEqual(len(Review.objects.all()), 1)
        # test update
        response = self.client.post(
            reverse('store:handle_review'),
            {
                'product_id': 1,
                'rating': 5,
                'review': 'test review update',
                'action': 'update'
            },
            xhr=True
        )
        self.assertEqual(
            response.json(),
            {
                'msg': 'Post updated',
                'rating': '5',
                'review': 'test review update'
            }
        )
        # test delete
        response = self.client.post(
            reverse('store:delete_review'),
            {
                'product_id': 1,
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(
            response.json(),
            {
                'msg': 'Deleted Succesfully',
            }
        )
        self.assertEqual(len(Review.objects.all()), 0)

    def test_add_review_not_first(self):
        """
        checking that there is already 
        a review from user
        """
        self.product.rating_score = 5
        self.product.rating_count = 1
        self.product.save()

        response = self.client.post(
            reverse('store:handle_review'),
            {
                'product_id': self.product.id,
                'rating': 3,
                'review': 'test review',
                'action': 'post'
            },
            xhr=True
        )
        self.assertEqual(
            response.json(),
            {
                'msg': 'Post created',
                'rating': '3',
                'review': 'test review'
            }
        )

    def test_search(self):
        """test search view"""
        response = self.client.post(
            reverse('store:search'),
            {
                'term': 'django',
            },
        )
        self.assertInHTML(
            '''<span class="badge badge-danger badge-danger-2
              rounded-pill px-4 py-2 font-weight-light">Django</span>''',
            response.content.decode()
        )
        response = self.client.post(
            reverse('store:search'),
            {
                'term': '',
            },
        )
        self.assertInHTML(
            '''<span class="badge badge-danger badge-danger-2
              rounded-pill px-4 py-2 font-weight-light"></span>''',
            response.content.decode()
        )
        response = self.client.post(
            reverse('store:search'),
            {
                'term': 'jsdf',
            },
        )
        self.assertInHTML(
            '''<span class="badge badge-danger badge-danger-2
              rounded-pill px-4 py-2 font-weight-light">Jsdf</span>''',
            response.content.decode()
        )
        response = self.client.get(reverse('store:search'))
        self.assertEqual(response.status_code, 200)
