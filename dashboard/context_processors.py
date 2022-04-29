from orders.models import OrderItem
from .models import Profile
from django.contrib.auth.models import User

def purchases(request):
    if request.user.is_authenticated:
        c_purchases = OrderItem.objects.all().filter(
            customer=request.user).distinct('product')
    else:
        c_purchases = None
    return ({'purchases': c_purchases})

def billing_info(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return ({'billing': profile})
    return ({'billing': None})

