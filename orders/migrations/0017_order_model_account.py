# Generated by Django 5.0.4 on 2024-07-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_order_items_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_model',
            name='account',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
