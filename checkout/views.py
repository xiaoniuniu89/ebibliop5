import os
import json
from django.http.response import HttpResponse
if os.path.isfile('env.py'):
    import env

import stripe

from basket.basket import Basket
from orders.views import payment_confirmation
from promotions.forms import PromoForm

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
if os.path.isfile('env.py'):
    import env

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


@login_required
def checkout(request):
    """ view to create a checkout intent on stripe """
    basket = Basket(request)
    promo_form = PromoForm()
    total = str(basket.get_total_price_after_discount()).replace('.', '')
    total = int(total)
    intent = stripe.PaymentIntent.create(
            amount=total,
            currency='eur',
            # payment_method_types=["card"],
            automatic_payment_methods={
                'enabled': True,
            },
            metadata={'userid': request.user.id}
        )
    return render(request, 'checkout/checkout.html', {'client_secret': intent.client_secret, 'promo_form': promo_form, 'intent': intent})


def checkout_complete(request):
    """ redirect page after successful order """
    basket = Basket(request)
    basket.clear()
    return render(request, 'checkout/checkout_complete.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        print('here')
        return HttpResponse(status=400)
    
    # Handle the event
    if event.type == 'payment_intent.succeeded':
        print('hello from event')
        payment_confirmation(event.data.object.client_secret)

    else:
        print(f'Unhandled event type {event.type}')

    return HttpResponse(status=200)

