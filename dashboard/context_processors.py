from orders.models import OrderItem

def purchases(request):
    if request.user.is_authenticated:
        purchases = OrderItem.objects.filter(
            customer=request.user).values('product').distinct()
    else:
        purchases = None
    return ({'purchases': purchases})
