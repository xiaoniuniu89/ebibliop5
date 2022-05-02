from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Message


def dashboard(request):
    """ Depending on user status will render to a different part of the site"""
    if request.user.is_superuser:
        return redirect('admin:index')
    elif request.user.is_staff:
        return redirect("store_admin:index")
    return render(request, 'dashboard/dashboard.html')


def send_message(request):
    """ view to handle the contact form in the footer """
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        content = request.POST.get('content')
        Message.objects.create(
            email=email,
            content=content
        )
        response = JsonResponse({'msg': 'your message has been sent'})
        return response
