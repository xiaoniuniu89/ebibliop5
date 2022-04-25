from orders.models import OrderItem

def purchases(request):
    if request.user.is_authenticated:
        c_purchases = OrderItem.objects.all().filter(
            customer=request.user).distinct('product')
    else:
        purchases = None
    return ({'purchases': c_purchases})
