# Generated by Django 3.2 on 2022-05-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_promo_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='promo_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
