from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Message
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ creates a profile when a user registers for the site """
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Message)
def send_mail(sender, instance, **kwargs):
    """ sends admin an email when a user fills out contact us form """
    message = instance
    message = render_to_string("contact_us_notification_email.html", {'message': message})
    mail = EmailMessage(
        subject=f'Message from {message.email}',
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER, ],
    )
    mail.content_subtype = "html"
    return mail.send()
