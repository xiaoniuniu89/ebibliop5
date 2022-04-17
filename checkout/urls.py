from django.urls import path

from .views import (
    checkout,
    checkout_complete
)

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout-complete/', checkout_complete, name='checkout_complete'),
]