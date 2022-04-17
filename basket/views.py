from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .basket import Basket
from store.models import Product

# Create your views here.

def basket_summary(request):
    """ returns a summary of items in users basket"""
    return render(request, 'basket/basket_summary.html')

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