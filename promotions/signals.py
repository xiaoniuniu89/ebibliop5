from django.core.mail import EmailMessage
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.contrib.auth.models import User
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
        mail.send()

@receiver(pre_save, sender=Subscriber)
def create_slug(sender, instance, **kwargs):
    """
    make unique slug for subscriber model
    """
    instance.slug = instance.email + str(instance.slug_end)
