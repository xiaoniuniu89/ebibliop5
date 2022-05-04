from django.shortcuts import render
from django.http import JsonResponse
import os
from basket.basket import Basket
from .models import Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User


# Create your views here.
def add_order(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = User.objects.get(username="guest_checkout").id
        order_key = request.POST.get('order_key')
        name = request.POST.get('name')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')
        basket_total = basket.get_total_price()

        # check order exists already
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name=name,
                address1=address1,
                address2=address2,
                country=country,
                city=city,
                post_code=postcode,
                total_price=basket_total,
                order_key=order_key
            )
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item['product'],
                    price=item['price'],
                    customer=order.user
                )
        response = JsonResponse({'success': 'Return Something'})
        return response


def payment_confirmation(data):
    """ post webhook payment confirmation view """
    Order.objects.filter(order_key=data).update(billing_status=True)
    order = Order.objects.get(order_key=data)
    order_items = OrderItem.objects.filter(order=order)
    order_items_url = [item.product.pdf.url for item in order_items]
    subject, from_email, to = 'Your E-biblio books', settings.EMAIL_HOST_USER, order.user.email
    text_message = f'Hi there, {order.full_name}. Your payment with E-biblio was successful. Here are your books, {"".join(order_items_url)} Enjoy 20% off your next purchase with the discount code EBIBLIO20.'
    html_message = get_template(("email.html")).render({
        'order': order,
        'order_items': order_items
    })
    message = EmailMultiAlternatives(subject, text_message, from_email, [to])
    message.attach_alternative(html_message, "text/html")
    message.send()


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

def test_email(request):
    order = Order.objects.get(order_key='pi_3Kv79OIaE0NFUuue2Z9wWc3Q_secret_fSK59mjCyS5Z0xOTWioG82HjG')
    # order.billing_status = True
    order_items = OrderItem.objects.filter(order=order)
    order_items_url = [item.product.pdf.url for item in order_items]
    subject, from_email, to = 'Your E-biblio books', settings.EMAIL_HOST_USER, order.user.email
    text_message = f'Hi there, {order.full_name}. Your payment with E-biblio was successful. Here are your books, {"".join(order_items_url)} Enjoy 20% off your next purchase with the discount code EBIBLIO20.'
    html_message = get_template(("email.html")).render({
        'order': order,
        'order_items': order_items
    })
    message = EmailMultiAlternatives(subject, text_message, from_email, [to])
    message.attach_alternative(html_message, "text/html")
    return render(request, 'email.html', {'order': order, 'order_items': order_items})