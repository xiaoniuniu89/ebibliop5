from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings


from .models import Product


@receiver(post_save, sender=Product)
def add_image_url(sender, instance, **kwargs):
    """
    Add image url after upload to aws
    """
    Product.objects.filter(id=instance.id).update(image_url=instance.image.url)
    