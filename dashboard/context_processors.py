from orders.models import OrderItem

from .models import Profile


def purchases(request):
    """
    gets any purchase items that the user
    has purchased in the past
    """
    if request.user.is_authenticated:
        c_purchases = OrderItem.objects.all().filter(
            customer=request.user).distinct('product')
    else:
        c_purchases = None
    return ({'purchases': c_purchases})


def billing_info(request):
    """gets any billing info on the current user"""
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return ({'billing': profile})
    return ({'billing': None})
