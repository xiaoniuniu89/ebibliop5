from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product, Review
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, View
from django.http import JsonResponse
import random

def landing(request):
    """ render store landing page """
    products = Product.products.all()[0:8]
    return render(request, 'store/landing.html', {'products': products})


class AllBooks(ListView):
    """
    Render all books 
    """
    queryset = Product.products.all()
    context_object_name = 'products'
    paginate_by = 12
    template_name = ('store/category.html')
    
    
def product_detail(request, slug):
    """ render product detail page """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    if product.get_rating():
        rating = product.get_rating()
        full_star, half_star = rating
        full_star = [x for x in range(full_star)]

    else:
        full_star = None
        half_star = None

    try:
        reviews = Review.objects.filter(
            product=product).exclude(user=request.user)
    except TypeError:
        reviews = Review.objects.all()
    try:
        user_review = Review.objects.filter(
            user=request.user, product=product)[0]
    except IndexError:
        user_review = None
    except TypeError:
        user_review = None
    return render(
        request,
        'store/detail.html',
        {'product': product, 'reviews': reviews, 'user_review': user_review, 'full_star': full_star, 'half_star': half_star})

def handle_review(request):
    """ Ajax call to handle creating and updating a review """
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        
        user = User.objects.get(id=request.user.id)
        rating = request.POST.get('rating')
        review = request.POST.get('review').strip()
        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            review=review
        )
        if product.get_rating():
            product_rating = product.get_rating()
            product.rating_score += int(rating)
            product.rating_count += 1

        else:
            product.rating_count = 1
            product.rating_score = int(rating)
        product.save()
        response = JsonResponse({'rating': rating, 'review': review})
        return response
    
    if request.POST.get('action') == 'update':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(id=request.user.id)
        rating = request.POST.get('rating')
        review = request.POST.get('review').strip()
        instance = Review.objects.filter(user=user, product=product)[0]
        product.rating_score -= int(instance.rating)
        instance.rating = rating
        product.rating_score += int(instance.rating)
        product.save()
        instance.review = review
        instance.save()

        response = JsonResponse({'rating': rating, 'review': review})
        return response

def delete_review(request):
    """ Ajax Call to delete users review """
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        user = User.objects.get(id=request.user.id)
        review = get_object_or_404(Review, product=product, user=user)
        product.rating_score -= int(review.rating)
        product.rating_count -= 1
        product.save()
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
        result = True
        if not products:
            result = False
            products = random.sample(list(Product.objects.all()), 8)
        if term.strip() == '':
            term = ''
            result = False
            products = random.sample(list(Product.objects.all()), 8)
        return render(
            request,
            'store/search.html',
            {'term': term, 'products': products, 'result': result}

        )
    else:
        return render(
            request,
            'store/search.html'
        )

