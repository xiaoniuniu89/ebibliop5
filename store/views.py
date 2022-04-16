from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def landing(request):
    """ render stoe landing page """
    products = Product.products.all()
    return render(request, 'store/landing.html', {'products': products})

def product_detail(request, slug):
    """ render product detail page """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/detail.html', {'product': product})

def category_list(request, category_slug):
    """ render list of books in a category """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        'store/category.html',
        {'category': category, 'products': products})
