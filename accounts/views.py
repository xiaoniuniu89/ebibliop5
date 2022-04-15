from django.shortcuts import render

# Create your views here.


def dashboard(request):
    """ render user dashboard"""
    return render(request, 'accounts/dashboard.html')
