from django.shortcuts import render
from .models import Category, Product

def landing(request):
    """ render stoe landing page """
    products = Product.products.all()
    return render(request, 'store/landing.html', {'products': products})
