# Generated by Django 4.2.5 on 2023-10-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='Model',
            new_name='model',
        ),
    ]
