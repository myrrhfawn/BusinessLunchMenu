# Generated by Django 4.2.3 on 2023-07-11 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_order_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dish_id',
            new_name='dish',
        ),
    ]
