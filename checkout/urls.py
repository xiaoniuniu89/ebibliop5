from django.urls import path
from django.views.generic import TemplateView

from .views import (
    checkout,
    checkout_complete,
    checkout_failed,
    stripe_webhook
)

app_name = 'checkout'

urlpatterns = [
    path(
        '',
        checkout,
        name='checkout'),
    path(
        'checkout-complete/',
        checkout_complete,
        name='checkout_complete'),
    path(
        'checkout-failed/',
        TemplateView.as_view(
            template_name='checkout/failed.html'),
        name='checkout_failed'),
    path(
        'error/',
        checkout_failed,
        name='checkout_failed'),
    path(
        'webhook/',
        stripe_webhook,
        name='webhook'),
]
