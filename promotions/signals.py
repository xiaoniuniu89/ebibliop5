from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings


from .models import NewsLetter


@receiver(post_save, sender=NewsLetter)
def send_newsletter(sender, instance, **kwargs):
    """
    Send newsletter to users on the site.
    """
    users = User.objects.exclude(username='admin')
    users = [user.email for user in users]
    print(users)
    message = instance
    message = render_to_string("newsletter.html", {'message': message})
    mail = EmailMessage(
        subject="E-biblio Newsletter",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=users,
    )
    mail.content_subtype = "html"
    return mail.send()