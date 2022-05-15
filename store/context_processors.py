import django.apps
from .models import Category

def all_categories(request):
    """ returns all categories of books"""
    return {
        'categories_list': Category.objects.all()
    }
