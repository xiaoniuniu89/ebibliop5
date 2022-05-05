from django.urls import path

from .views import (
    dashboard,
    send_message,
    update_billing
)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('update-billing', update_billing, name='update_billing_info'),
    path('contact-us', send_message, name='send_message'),
]
