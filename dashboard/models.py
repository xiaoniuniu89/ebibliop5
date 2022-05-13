from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField



# extends user model
class Profile(models.Model):
    """
    A profile is created through signals.py whenever
    a user signs up for an account
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    postcode = models.CharField(max_length=15, blank=True)
    address_line_one = models.CharField(max_length=150, blank=True)
    address_line_two = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    billing_email = models.EmailField(default='')

    # for admin page

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user}\'s profile'

class Message(models.Model):
    """
    A class to handle user submissions 
    of the contact us form in the footer
    """

    email = models.EmailField()
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta data for messages """
        verbose_name_plural = 'Messages'
        ordering = ('-date_posted',)
    
    def __str__(self):
        return f'Message from {self.email}'
