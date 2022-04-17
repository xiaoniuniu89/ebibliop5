from django.urls import path

from .views import (
    basket_summary,
    basket_add,
    basket_delete
)

app_name = 'basket'

urlpatterns = [
    path('', basket_summary, name='basket_summary'),
    path('add/', basket_add, name='basket_add'),
    path('delete/', basket_delete, name='basket_delete'),
]
