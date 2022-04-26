from django.urls import path
from .views import (
    promo
)

app_name = 'promotions'

urlpatterns = [
    path('', promo, name='promotions'),
]
