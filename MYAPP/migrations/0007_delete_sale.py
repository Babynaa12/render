# Generated by Django 5.1.4 on 2025-01-26 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MYAPP', '0006_remove_payment_payment_method'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
