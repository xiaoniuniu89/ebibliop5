from django.urls import path

from .views import (
    add_order,
    GenerateInvoice,
)

app_name = 'orders'

urlpatterns = [
    path('add/', add_order, name='add_order'),
    path('invoice/<int:pk>/', GenerateInvoice.as_view(), name='invoice'),
]
