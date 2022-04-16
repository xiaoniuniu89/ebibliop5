from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product_creator'
    )
    title = models.CharField(max_length=255, default='admin')
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='images/default.png'
    )
    pdf = models.FileField(upload_to='pdf/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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
