from decimal import Decimal

from django.db import models

from django.contrib.auth.models import User

from store.models import Product

from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='order_user'
    )
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    country = models.CharField(max_length=50, default='Ireland')
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='order_item_user',
        null=True
    )

    def __str__(self):
        return str(self.id)