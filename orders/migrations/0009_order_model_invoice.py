# Generated by Django 5.0.4 on 2024-07-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_model_ph_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_model',
            name='invoice',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
