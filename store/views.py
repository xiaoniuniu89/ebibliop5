from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product, Review
from django.http import JsonResponse
from django.contrib.auth.models import User

def landing(request):
    """ render stoe landing page """
    products = Product.products.all()
    return render(request, 'store/landing.html', {'products': products})

def product_detail(request, slug):
    """ render product detail page """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    reviews = Review.objects.filter(product=product).exclude(user=request.user)
    try:
        user_review = Review.objects.filter(user=request.user, product=product)[0]
    except IndexError:
        user_review = None
    return render(
        request,
        'store/detail.html',
        {'product': product, 'reviews': reviews, 'user_review': user_review})

def add_review(request):
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        print(product_id)
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(id=request.user.id)
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            review=review
        )
        response = JsonResponse({'rating': rating, 'review': review})
        return response

def delete_review(request):
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        user = User.objects.get(id=request.user.id)
        review = get_object_or_404(Review, product=product, user=user)
        review.delete()
        response = JsonResponse({'msg': 'Deleted Succesfully'})
        return response





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

