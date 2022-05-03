from django.shortcuts import render
from django.http import JsonResponse
import os
from basket.basket import Basket
from .models import Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def add_order(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
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
                    customer=request.user
                )
        response = JsonResponse({'success': 'Return Something'})
        return response


def payment_confirmation(data):
    """ post webhook payment confirmation view """
    order = Order.objects.get(order_key=data)
    order.billing_status = True
    order_items = OrderItem.objects.filter(order=order)
    message = get_template("email.html").render({
        'order': order,
        'order_items': order_items
    })
    # order_items_url = [item.product.pdf.url for item in order_items]
    # print(order_items_url)
    send_mail(
        subject='Your E-biblio order',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.user.email, ],
        fail_silently=False,
    )


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

def test_email(request):
    order = Order.objects.get(order_key='pi_3Kv79OIaE0NFUuue2Z9wWc3Q_secret_fSK59mjCyS5Z0xOTWioG82HjG')
    # order.billing_status = True
    order_items = OrderItem.objects.filter(order=order)
    # order_items_url = [item.product.pdf.url for item in order_items]
    # print(order_items_url)
    message = get_template("email.html").render({
        'order': order,
        'order_items': order_items
    })
    send_mail(
        subject='Your E-biblio books',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.user.email, ],
        fail_silently=False,
    )
    return render(request, 'email.html', {'order': order, 'order_items': order_items})

# order = Order.objects.get(order_key='pi_3Kv79OIaE0NFUuue2Z9wWc3Q_secret_fSK59mjCyS5Z0xOTWioG82HjG')
# order_items = OrderItem.objects.filter(order=order)
# order_items = [item.product for item in order_items]
# def return_items(x):
#     new_list = []
#     for book in x:
#         book = f'<a href="{book.pdf.url}" target="_blank">{book.title}</a>'
#         new_list.append(book)
#     return new_list
# order_items = return_items(order_items)
# message = f'Hi there, {order.full_name}. Your payment with E-biblio was successful. Here are your books, {"".join(order_items)} Enjoy 20% off your next purchase with the discount code EBIBLIO20.'
# text = f'''
# <html>
#     <body>
#         <h1>Testing</h1>
#         <p>{message}</p>
#     </body>
# </html>
# '''

# file = open("sample.html","w")
# file.write(text)
# file.close()