from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Promo, Subscriber
from .forms import PromoForm
from django.http import JsonResponse
from basket.basket import Basket
import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

def promo(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        promo_code = request.POST.get('promo_code')
        promo_code = Promo.objects.get(code=promo_code)
        basket.add_promo(promo_code.discount)
        discount = basket.get_discount()
        total = basket.get_total_price_after_discount()
        response = JsonResponse({'code': basket.promo, 'discount': discount, 'total': total})
        return response

def subscribe(request):
    """ view to handle the subscribe form in the footer """
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            response = JsonResponse({'msg': 'email already subscribed!'})
            return response
        Subscriber.objects.create(
            email=email,
        )
        response = JsonResponse({'msg': 'email subscribed!'})
        return response