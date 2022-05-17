import os
import stripe

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from basket.basket import Basket

from .models import Promo, Subscriber


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def promo(request):
    """ handle adding promo code to basket"""
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        # get the promo name and use to
        # get promo from the database
        promo_code = request.POST.get('promo_code')
        promo_code = Promo.objects.get(code=promo_code)
        basket.add_promo(promo_code.discount)
        discount = basket.get_discount()
        # update basket total price
        total = basket.get_total_price_after_discount()
        response = JsonResponse(
            {'code': basket.promo, 'discount': discount, 'total': total})
        return response


def subscribe(request):
    """ view to handle the subscribe form in the footer """
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        # check if email is already subscribed
        if Subscriber.objects.filter(email=email).exists():
            response = JsonResponse({'msg': 'email already subscribed!'})
            return response
        Subscriber.objects.create(
            email=email,
        )
        response = JsonResponse({'msg': 'email subscribed!'})
        return response


class unsubscribe(DeleteView):
    """ view to handle the unsubscribing from newsletter """
    model = Subscriber
    success_url = reverse_lazy('promotions:unsubscribe_success')
