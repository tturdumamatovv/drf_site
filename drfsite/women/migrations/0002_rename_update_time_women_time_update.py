# Generated by Django 4.1.2 on 2022-10-14 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='update_time',
            new_name='time_update',
        ),
    ]