# Generated by Django 3.2.16 on 2022-11-01 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('party_size', models.IntegerField()),
            ],
        ),
    ]
