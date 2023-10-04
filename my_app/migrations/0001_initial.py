# Generated by Django 4.2.5 on 2023-10-01 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=27)),
                ('contact', models.CharField(max_length=15)),
                ('seat_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_no', models.CharField(max_length=40)),
                ('Model', models.CharField(max_length=30)),
                ('Brand', models.CharField(max_length=30)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField()),
                ('departure_time', models.IntegerField()),
                ('departure_place', models.CharField(max_length=22)),
                ('destination', models.CharField(max_length=22)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_date', models.DateField()),
                ('amount_paid', models.IntegerField()),
                ('received_by', models.CharField(max_length=26)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=28)),
                ('address', models.CharField(max_length=26)),
                ('contact', models.CharField(max_length=14)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.bus')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.trip'),
        ),
    ]