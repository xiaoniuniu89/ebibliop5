# Generated by Django 3.2 on 2022-05-03 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_slug_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_end',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
