from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Promo
from .forms import PromoForm
from django.http import JsonResponse
from basket.basket import Basket
import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
# @require_POST
# def promo(request):
#     now = timezone.now()
#     form = PromoForm(request.post)
#     if form.is_valid():
#         code = form.cleaned_data['code']
#         try:
#             promo_code = Promo.objects.get(
#                 code__iexact=code,
#             )
#             request.session['promo_id'] = promo_code.id
#         except Promo.DoesNotExist:
#             request.session['promo_id'] = None
#     return redirect('checkout:checout')

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
