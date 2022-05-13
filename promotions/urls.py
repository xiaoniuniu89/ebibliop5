from django.urls import path
from .views import (
    promo,
    subscribe
)

app_name = 'promotions'

urlpatterns = [
    path('', promo, name='add_promo'),
    path('subscribe', subscribe, name='subscribe'),
]
