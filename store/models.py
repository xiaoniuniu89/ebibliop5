from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import image_resize, unique_slugify
from django.utils.text import slugify
from dashboard.models import Profile
from django.urls import reverse
import uuid

class ProductManager(models.Manager):
    """ manager to replace objects manager """
    def get_queryset(self):
        """ returns products that are in stock """
        return super(ProductManager, self).get_queryset().filter(in_stock=True)


class Category(models.Model):
    """ gives each book a category for sorting/browsing purposes"""
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        """ Meta data for Category class """
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        """ method for returning Category url """
        return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """ Database tables for Products """
    category = models.ForeignKey(
        Category, related_name='product',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
    )
    pdf = models.FileField(upload_to='pdf/', blank=False)
    slug = models.SlugField(max_length=255)
    slug_end = models.UUIDField(default=uuid.uuid4)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating_score = models.IntegerField(null=True)
    rating_count = models.IntegerField(null=True)
    objects = models.Manager()
    products = ProductManager()
    
    class Meta:
        """ Meta data for product """
        verbose_name_plural = 'Products'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        """ returns url for product detail page """
        return reverse("store:product_detail", args=[self.slug])
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image_resize(self.image, 512, 512)
        # if Product.objects.filter(slug=self.slug).exists():
        #     self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)


    

    def get_rating(self):
        """ get average rating of a product """
        try:
            return (divmod(self.rating_score, self.rating_count))
        except ZeroDivisionError:
            return None


class Review(models.Model):
    """ model to create reviews and ratings on individual products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(max_length=800, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_on', '-created_on', )

    def __str__(self):
        return f'review for {self.product} by {self.user}'
    
    
