# Generated by Django 4.2.5 on 2023-11-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_remove_trip_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]