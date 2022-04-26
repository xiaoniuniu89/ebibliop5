from django.shortcuts import render

# Create your views here.

def promo(request):
    return render(request, 'store/landing.html')