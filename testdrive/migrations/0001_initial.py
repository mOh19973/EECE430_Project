# Generated by Django 2.0.3 on 2018-04-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TDModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('carName', models.CharField(max_length=20)),
                ('day', models.IntegerField(max_length=20)),
                ('month', models.IntegerField(max_length=20)),
                ('year', models.IntegerField(max_length=20)),
                ('hour', models.IntegerField(max_length=20)),
                ('minutes', models.IntegerField(max_length=20)),
            ],
        ),
    ]
