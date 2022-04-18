from django.shortcuts import render
from django.http import JsonResponse

from basket.basket import Basket
from .models import Order, OrderItem


# Create your views here.
def add_order(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        basket_total = basket.get_total_price()

        # check order exists already
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name='name',
                address1='add1',
                address2='add2',
                total_price=basket_total,
                order_key=order_key
            )
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item['product'],
                    price=item['price'],
                    customer=request.user
                )
        response = JsonResponse({'success': 'Return Something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)
