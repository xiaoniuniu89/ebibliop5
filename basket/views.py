from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket

# Create your views here.


def basket_summary(request):
    """ returns a summary of items in users basket"""
    basket = Basket(request)
    return render(request, 'basket/basket_summary.html', {'basket': basket})


def basket_add(request):
    """ ajax request to add items to basket """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price_after_discount()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
