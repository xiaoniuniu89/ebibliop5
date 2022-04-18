from orders.models import OrderItem

def purchases(request):
    purchases = OrderItem.objects.filter(customer=request.user)
    return ({'purchases': purchases})