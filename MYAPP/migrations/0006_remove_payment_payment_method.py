# Generated by Django 5.1.4 on 2025-01-17 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MYAPP', '0005_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_method',
        ),
    ]
