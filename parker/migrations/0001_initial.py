# Generated by Django 4.2.7 on 2023-11-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_row', models.IntegerField()),
                ('slot_column', models.IntegerField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('car_no', models.CharField(max_length=20)),
                ('payment', models.FloatField()),
                ('customer_Id', models.IntegerField(max_length=20)),
                ('parking_Id', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Buisness_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('upi_Id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('parking_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Parking_lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('length', models.FloatField(max_length=20)),
                ('width', models.FloatField(max_length=20)),
                ('Buisness_Id', models.IntegerField(max_length=20)),
            ],
        ),
    ]
