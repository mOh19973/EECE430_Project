# Generated by Django 2.0.2 on 2018-03-18 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20180318_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='Doors',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='Engine',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='FuelCapacity',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='HP',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='Mileage',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='TopSpeed',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='Weight',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='Year',
        ),
    ]
