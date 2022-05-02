from .models import Category
import django.apps

def all_categories(request):
    """ returns all categories of books"""
    return {
        'categories_list': Category.objects.all()
    }



