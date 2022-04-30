from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product, Review


def landing(request):
    """ render stoe landing page """
    products = Product.products.all()
    return render(request, 'store/landing.html', {'products': products})

def product_detail(request, slug):
    """ render product detail page """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    reviews = Review.objects.filter(product=product)
    return render(request, 'store/detail.html', {'product': product, 'reviews': reviews})

def category_list(request, category_slug):
    """ render list of books in a category """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        'store/category.html',
        {'category': category, 'products': products})

def search(request):
    """ returns search results for a book from search bar in nav"""
    if request.method == 'POST':
        term = request.POST['term'].lstrip().rstrip().split(
                " ")[0]
        products = Product.objects.filter(
            Q(title__icontains=term) |
            Q(author__icontains=term)
        )
        return render(
            request,
            'store/search.html',
            {'term': term, 'products': products}

        )
    else:
        return render(
            request,
            'store/search.html'
        )

