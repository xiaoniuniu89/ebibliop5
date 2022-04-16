from django.urls import path
from .views import (
    landing,
    product_detail,
    category_list,
)

app_name = 'store'

urlpatterns = [
    path('', landing, name='landing'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),
]
