from django.shortcuts import render
from django.http import JsonResponse

from .models import Message

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def send_message(request):
    if request.POST.get('action') == 'post':
        email = request.POST.get('email')
        content = request.POST.get('content')
        Message.objects.create(
            email=email,
            content=content
        )
        response = JsonResponse({'msg': 'your message has been sent'})
        return response
