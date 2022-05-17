from django.http import JsonResponse
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from basket.basket import Basket

from .models import Order, OrderItem
from .utils import render_to_pdf


def add_order(request):
    """ajax call to create an order before making payment"""
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        # if user is logged in use their profile
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            # if guest use the guest_checkout profile
            user_id = User.objects.get(username="guest_checkout").id
        # get POST variables
        order_key = request.POST.get('order_key')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')
        promo = basket.get_discount()
        basket_total = basket.get_total_price_after_discount()

        # check order exists already
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            # make one
            order = Order.objects.create(
                user_id=user_id,
                full_name=name,
                email=email,
                address1=address1,
                address2=address2,
                country=country,
                city=city,
                post_code=postcode,
                total_price=basket_total,
                promo_total=promo,
                order_key=order_key
            )
            order_id = order.pk
            for item in basket:
                # make an order item for each item in order
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item['product'],
                    price=item['price'],
                    customer=order.user
                )
        response = JsonResponse({'success': 'order created'})
        return response


def payment_confirmation(data):
    """ post webhook payment confirmation view """
    # find order and update payment to True
    Order.objects.filter(order_key=data).update(billing_status=True)
    # find order items and send confirmation email containing links
    order = Order.objects.get(order_key=data)
    order_items = OrderItem.objects.filter(order=order)
    order_items_url = [item.product.pdf.url for item in order_items]
    subject = 'Your E-biblio books'
    from_email = settings.EMAIL_HOST_USER
    to = order.email
    text_message = f'''
        Hi there, {order.full_name}. Your payment with E-biblio was successful.
        Here are your books,{"".join(order_items_url)} Enjoy 30% off your next
        purchase with the discount code EBIBLIO30.'''
    html_message = get_template(("email.html")).render({
        'order': order,
        'order_items': order_items
    })
    message = EmailMultiAlternatives(subject, text_message, from_email, [to])
    message.attach_alternative(html_message, "text/html")
    message.send()


class GenerateInvoice(UserPassesTestMixin, View):
    """generate a pdf invoice of past orders"""

    def get(self, request, pk, *args, **kwargs):
        """ view to generate a pdf invoice of customer orders """
        order = Order.objects.get(pk=pk)
        order_items = OrderItem.objects.filter(order=order)
        pdf = render_to_pdf('orders/invoice.html',
                            {'order': order, 'order_items': order_items})
        return HttpResponse(pdf, content_type='application/pdf')

    def test_func(self):
        # check the order customer is the request user
        pk = self.kwargs['pk']
        return self.request.user == Order.objects.get(pk=pk).user
