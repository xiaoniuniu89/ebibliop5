import random

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import ListView

from orders.models import OrderItem

from .models import Category, Product, Review


def landing(request):
    """ render store landing page """
    # products.all() means all products in stock
    # order is by rating score - so the first 8
    # being the 8 highest rated books by score
    products = Product.products.all()[0:8]
    return render(request, 'store/landing.html',
                  {'products': products, 'title': 'Home'})


class AllBooks(ListView):
    """
    Render all books for categories => all books
    """
    queryset = Product.products.all()
    context_object_name = 'products'
    paginate_by = 12
    template_name = ('store/category.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'All Books'
        return context


def product_detail(request, slug):
    """
    render product detail page
    User can leave review if logged in and
    has bought the product in the past
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    if request.user.is_authenticated:
        # check if user is logged in
        if OrderItem.objects.filter(
            # check user has bought this book already
            customer=request.user, product=product).exists():
            can_review = True
        else:
            can_review = False
    else:
        can_review = False
    if product.get_rating():
        # rating from returned divmod
        # half star will be remainder
        rating = product.get_rating()
        full_star, half_star = rating
        # get count of quotient
        full_star = [x for x in range(full_star)]

    else:
        # no rating found
        full_star = None
        half_star = None

    try:
        reviews = Review.objects.filter(
            product=product).exclude(user=request.user)
    except TypeError:
        # reviews exist, but none from user
        reviews = Review.objects.filter(product=product)
    try:
        user_review = Review.objects.filter(
            user=request.user, product=product)[0]
    except IndexError:
        # no review from request user
        user_review = None
    except TypeError:
        # no review from user not logged in
        user_review = None
    return render(request,
                  'store/detail.html',
                  {'product': product,
                   'reviews': reviews,
                   'user_review': user_review,
                   'full_star': full_star,
                   'half_star': half_star,
                   'title': product.title,
                   'can_review': can_review})


def handle_review(request):
    """ Ajax call to handle creating and updating a review """
    if request.POST.get('action') == 'post':
        # post = create review
        # get POST variables
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(id=request.user.id)
        rating = request.POST.get('rating')
        review = request.POST.get('review').strip()
        # create new review
        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            review=review
        )
        # add to rating score if exists
        if product.get_rating():
            product_rating = product.get_rating()
            product.rating_score += int(rating)
            product.rating_count += 1

        else:
            # create a rating score
            product.rating_count = 1
            product.rating_score = int(rating)
        product.save()
        msg = 'Post created'
        response = JsonResponse(
            {'rating': rating, 'review': review, 'msg': msg})
        return response

    if request.POST.get('action') == 'update':
        # update = update review
        # get POST variables
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(id=request.user.id)
        rating = request.POST.get('rating')
        review = request.POST.get('review').strip()
        instance = Review.objects.filter(user=user, product=product)[0]
        # before saving the updated review
        # delete the old review score
        product.rating_score -= int(instance.rating)
        instance.rating = rating
        # save the new review score
        product.rating_score += int(instance.rating)
        product.save()
        instance.review = review
        instance.save()
        msg = 'Post updated'

        response = JsonResponse(
            {'rating': rating, 'review': review, 'msg': msg})
        return response


def delete_review(request):
    """ Ajax Call to delete users review """
    if request.POST.get('action') == 'post':
        # get POST variables
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        user = User.objects.get(id=request.user.id)
        review = get_object_or_404(Review, product=product, user=user)
        # remove rating score
        product.rating_score -= int(review.rating)
        product.rating_count -= 1
        product.save()
        review.delete()
        response = JsonResponse({'msg': 'Deleted Succesfully'})
        return response


def category_list(request, category_slug):
    """ render list of books in a category """
    # help for this view from the following tutorial from very academy
    # https://www.youtube.com/watch?v=UqSJCVePEWU beginning at 1hr and 59 minutes
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        'store/category.html',
        {'category': category, 'products': products, 'title': category})


def search(request):
    """ returns search results for a book from search bar in nav"""
    if request.method == 'POST':
        # strip whitespace from search term
        term = request.POST['term'].lstrip().rstrip().split(
            " ")[0]
        products = Product.objects.filter(
            Q(title__icontains=term) |
            Q(author__icontains=term)
        )
        # result true will show term results
        result = True
        if not products:
            # false will show recommendations instead
            result = False
            try:
                # give random selection
                products = random.sample(list(Product.objects.all()), 8)
            except ValueError:
                # if not 8 products return all products
                products = Product.objects.all()
        if term.strip() == '':
            # if term is empty return false
            term = ''
            result = False
            try:
                # return 8
                products = random.sample(list(Product.objects.all()), 8)
            except ValueError:
                # else return all
                products = Product.objects.all()
        return render(request,
                      'store/search.html',
                      {'term': term,
                       'products': products,
                       'result': result,
                       'title': f'search {term}'})
    else:
        # if user goes to search page from url bar
        return render(
            request,
            'store/search.html'
        )


def handle_404(request, exception):
    """custom 404 page"""
    return render(request, '404.html')


def handle_500(request):
    """custom server error page"""
    return render(request, '500.html')


def handle_403(request, exception):
    """custom 403 forbidden page"""
    return render(request, '403.html')


def handle_400(request, exception):
    """custom 400 bad request page"""
    return render(request, '400.html')
