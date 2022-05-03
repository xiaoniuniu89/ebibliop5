from django.urls import path

from .views import (
    add_order,
    test_email
)

app_name = 'orders'

urlpatterns = [
    path('add/', add_order, name='add_order'),
    path('email/', test_email, name='test_email'),
]
