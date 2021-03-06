from django.core.mail import EmailMessage
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from .models import NewsLetter, Subscriber


@receiver(post_save, sender=NewsLetter)
def send_newsletter(sender, instance, **kwargs):
    """
    Send newsletter to users on the site.
    """
    users = Subscriber.objects.all()
    emails = [user.email for user in users]
    for email in emails:
        message = instance
        # do it one by one in for loop
        # to avoid other users seeing email addresses
        # also because we need to send a unique
        # unsubscribe link to each user
        sub = Subscriber.objects.get(email=email)
        message = render_to_string(
            "newsletter.html",
            {'message': message, 'sub': sub}
        )
        mail = EmailMessage(
            subject="E-biblio Newsletter",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[email, ],
        )
        mail.content_subtype = "html"
        try:
            mail.send()
        # general exception needed to catch a
        # invalid email not caught in form
        # validation in footer - rare
        # exception
        except Exception:
            pass


@receiver(pre_save, sender=Subscriber)
def create_slug(sender, instance, **kwargs):
    """
    make unique slug for subscriber model
    """
    instance.slug = instance.email + str(instance.slug_end)
