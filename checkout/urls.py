from django.urls import path

from .views import (
    checkout,
    checkout_complete,
    checkout_failed,
    stripe_webhook
)

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout-complete/', checkout_complete, name='checkout_complete'),
    path('error/', checkout_failed, name='checkout_failed'),
    path('webhook/', stripe_webhook, name='webhook'),
]