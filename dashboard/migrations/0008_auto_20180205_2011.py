# Generated by Django 2.0.1 on 2018-02-05 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20180130_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddetail',
            name='timestamp',
            field=models.TimeField(default=datetime.time(20, 11, 4, 679671)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='end_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='start_time',
            field=models.CharField(max_length=200),
        ),
    ]