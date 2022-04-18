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

    # for admin page

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user}\'s profile'