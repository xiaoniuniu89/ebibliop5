from django.urls import path

from .views import (
    dashboard,
    send_message
)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('contact-us', send_message, name='send_message'),
]
