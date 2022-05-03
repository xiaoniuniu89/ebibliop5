from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

from ebiblio.settings import EMAIL_HOST_USER

from .models import NewsLetter


@receiver(post_save, sender=NewsLetter)
def send_newsletter(sender, instance, **kwargs):
    """
    Send newsletter to users on the site.
    """
    users = User.objects.exclude(username='admin')
    users = [user.email for user in users]
    message = instance
    message = get_template("newsletter.html").render(Context({
        'message': message.get_serialized_data()
    }))
    mail = EmailMessage(
        subject="E-biblio Newsletter",
        body=message,
        from_email=EMAIL_HOST_USER,
        to=[users],
    )
    mail.content_subtype = "html"
    return mail.send()