import factory
from store.models import Product, Category


class YourModelFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = models.Product()
 
    image = factory.Django.ImageField()