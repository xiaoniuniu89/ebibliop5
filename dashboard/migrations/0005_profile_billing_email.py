# Generated by Django 3.2 on 2022-05-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='billing_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
