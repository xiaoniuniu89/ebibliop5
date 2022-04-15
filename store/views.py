from django.shortcuts import render

# Create your views here.


def landing(request):
    """ render stoe landing page """
    return render(request, 'store/landing.html')
