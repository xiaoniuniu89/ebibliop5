import os
if os.path.isfile('env.py'):
    import env

import stripe

from basket.basket import Basket

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# stripe.api_key = os.environ.get('STRIPE_PKEY')
stripe.api_key = 'sk_test_51KpZBDIaE0NFUuueXdekO83hHiKuRNt9WudV41X80buAyLzz0jT9JSsT1WYzZyxrldbnivqx9K6XK4ZxZyF9J8JG00IghjLq7C'

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
