from django.urls import path
from django.views.generic import TemplateView
from .views import (
    promo,
    subscribe,
    unsubscribe,
)

app_name = 'promotions'

urlpatterns = [
    path('', promo, name='add_promo'),
    path('subscribe/', subscribe, name='subscribe'),
    path('<str:slug>/unsubscribe/', unsubscribe.as_view(), name='unsubscribe'),
    path('unsubscribe/success/', TemplateView.as_view(template_name='promotions/unsubscribe_successful.html'), name='unsubscribe_success'),
]
