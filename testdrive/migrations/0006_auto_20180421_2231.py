# Generated by Django 2.0.3 on 2018-04-21 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdrive', '0005_auto_20180421_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdmodel',
            name='driveCar',
        ),
        migrations.RemoveField(
            model_name='tdmodel',
            name='driver',
        ),
    ]
