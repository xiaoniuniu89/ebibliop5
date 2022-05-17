from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse

import os
import json
import stripe

from basket.basket import Basket
from orders.views import payment_confirmation
from orders.models import Order

if os.path.isfile('env.py'):
    import env

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def checkout(request):
    """ view to create a checkout intent on stripe """
    basket = Basket(request)
    total = str(basket.get_total_price_after_discount()).replace('.', '')
    total = int(total)
    # get total price and check if it is at least the stripe minimum
    if total < 50:
        # if not, redirect to basket
        messages.warning(request, 'The minimum transaction is .50 cent')
        return HttpResponseRedirect('/basket/')
    if request.user.is_authenticated:
        # check if user has profile / billing info
        user_id = request.user.id
    else:
        # if not use guest checkout as proxy
        user_id = User.objects.get(username="guest_checkout").id
    # create payment intent with stripe
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='eur',
        automatic_payment_methods={
            'enabled': True,
        },
        # will use this later in webhook to update billing status
        metadata={'userid': user_id}
    )
    return render(
        request,
        'checkout/checkout.html',
        {
            'client_secret': intent.client_secret,
            'intent': intent,
            'title': 'Checkout'
        })


def checkout_complete(request):
    """ redirect page after successful order """
    basket = Basket(request)
    # empty basket
    basket.clear()
    return render(request,
                  'checkout/checkout_complete.html',
                  {'title': 'Checkout Complete'})


def checkout_failed(request):
    """ handle failed payments """
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        order = Order.objects.get(order_key=order_key)
        # make sure to delete order
        order.delete()
        msg = request.POST.get('error')
        response = JsonResponse({'msg': msg})
        return response


@csrf_exempt
def stripe_webhook(request):
    """listens for payment_intent.succeeded"""
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print(f'Unhandled event type {event.type}')

    return HttpResponse(status=200)
