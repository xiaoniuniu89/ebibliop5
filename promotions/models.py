from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

class Promo(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class NewsLetter(models.Model):
    user = models.ForeignKey(
        User,
        default='admin',
        on_delete=models.CASCADE)
    message = models.TextField(max_length=2000)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'newsletter from {self.user} on {self.date_created}'
