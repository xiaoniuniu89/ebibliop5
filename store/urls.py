from django.urls import path
from .views import (
    landing,
    product_detail,
    category_list,
    search,
    add_review
)

app_name = 'store'

urlpatterns = [
    path('', landing, name='landing'),
    path('shop/<slug:slug>/', product_detail, name='product_detail'),
    path('shop/review/add', add_review, name='add_review'),
    path('browse/<slug:category_slug>/', category_list, name='category_list'),
    path('search/', search, name='search'),
]
