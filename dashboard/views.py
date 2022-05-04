from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message, Profile


@login_required
def dashboard(request):
    """ Depending on user status will render to a different part of the site"""
    if request.user.is_superuser:
        return redirect('admin:index')
    elif request.user.is_staff:
        return redirect("admin:index")
    return render(request, 'dashboard/dashboard.html')

def update_billing(request):
    """ view to handle updatig billing info in dashboard """
    if request.POST.get('action') == 'post':
        username = request.POST.get('userName')
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        country = request.POST.get('country')
        city = request.POST.get('city')
        post_code = request.POST.get('postCode')
        user.first_name = first_name
        user.last_name = last_name
        profile.address_line_one = address1
        profile.address_line_two = address2
        profile.country = country
        profile.city = city
        profile.postcode = post_code
        user.save()
        profile.save()
        response = JsonResponse({'msg': 'updated succesfullys'})
        return response




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
