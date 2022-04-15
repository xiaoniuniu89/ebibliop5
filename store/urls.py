from django.urls import path
from .views import (
    landing,
)

app_name = 'store'

urlpatterns = [
    path('', landing, name='landing'),
]

