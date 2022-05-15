from django.contrib.auth.models import User
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from store.models import Category, Product, Review


small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


class TestCategoriesModel(TestCase):
    """test Category model"""

    def setUp(self):
        self.cat = Category.objects.create(name='django', slug='django')

    def test_category_model_instance(self):
        """Test category model"""
        data = self.cat
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """ Test __str__ """
        data = self.cat
        self.assertEquals(str(data), 'django')

    def test_category_model_get_absolute_url(self):
        """ Test get_absolute_url """
        data = self.cat
        self.assertEquals(str(data.get_absolute_url()), '/browse/django/')


class TestProductModel(TestCase):
    """Test the Product Model"""

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(
            title='django for life',
            slug='django-for-life',
            price='9.99',
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

    def test_product_model_instance(self):
        """Test product model instance"""
        data = self.product
        self.assertTrue(isinstance(data, Product))

    def test_product_model_name(self):
        """Test product model"""
        data = self.product
        self.assertEquals(str(data), 'django for life')

    def test_product_in_stock(self):
        """check product manager"""
        data = Product.products.all()
        self.assertEquals(len(data), 1)

    def test_product_model_get_absolute_url(self):
        """ Test get_absolute_url """
        data = self.product
        self.assertEquals(str(data.get_absolute_url()),
                          '/shop/django-for-life/')

    def test_product_model_get_rating(self):
        """ Test get_rating """
        data = self.product
        self.assertEquals(data.get_rating(), None)
        data.rating_count = 1
        data.rating_score = 4
        data.save()
        self.assertEquals(data.get_rating(), (4, 0))


class TestReviewgModel(TestCase):
    """Test the Review Model"""

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        self.product = Product.objects.create(
            title='django for life',
            slug='django-for-life',
            price='9.99',
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
        self.review = Review.objects.create(
            product=Product.objects.get(title=('django for life')),
            user=User.objects.create(
                username='admin',
                email='admin@mail.com',
                password='test12344321'
            ),
            rating=3,
            review='A test review'

        )

    def test_review_model_name(self):
        """ Test __str__ """
        data = self.review
        self.assertEquals(str(data), 'review for django for life by admin')
