from django.urls import path
from .views import (
    dashboard,
)

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]

