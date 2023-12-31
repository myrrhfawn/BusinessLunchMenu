# Generated by Django 4.2.3 on 2023-07-10 16:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='menu',
            name='days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3),
        ),
    ]
