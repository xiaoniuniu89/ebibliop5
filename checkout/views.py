import os
if os.path.isfile('env.py'):
    import env

import stripe

from basket.basket import Basket

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
if os.path.isfile('env.py'):
    import env

# stripe.api_key = os.environ.get('STRIPE_PKEY')
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@login_required
def checkout(request):
    """ view to create a checkout intent on stripe """
    basket = Basket(request)
    total = str(basket.get_total_price()).replace('.', '')
    total = int(total)
    intent = stripe.PaymentIntent.create(
            amount=total,
            currency='eur',
            automatic_payment_methods={
                'enabled': True,
            },
            metadata={'userid': request.user.id}
        )
    return render(request, 'checkout/checkout.html', {'client_secret': intent.client_secret})


def checkout_complete(request):
    """ redirect page after successful order """
    return render(request, 'checkout/checkout_complete.html')
