from django.urls import path

from .views import (
    basket_summary,
)

app_name = 'basket'

urlpatterns = [
    path('', basket_summary, name='basket_summary'),
]
