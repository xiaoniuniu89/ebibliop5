from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    """test Category model"""
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
        
    def test_category_model_instance(self):
        """Test category model"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_name(self):
        """ Test __str__ """
        data = self.data1
        self.assertEquals(str(data), 'django')
        
        
class TestProductModel(TestCase):
    """Test the Product Model"""
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django for life', created_by_id=1,
                                            slug='django-for-life', price='9.99', image='django')
        
    def test_product_model_instance(self):
        """Test product model instance"""
        data = self.data1
        self.assertTrue(isinstance(data, Product))
    
    def test_product_model_name(self):
        """Test product model"""
        data = self.data1
        self.assertEquals(str(data), 'django for life')
        
    def test_product_in_stock(self):
        """check product manager"""
        data = Product.products.all()
        self.assertEquals(len(data), 1)
        
        