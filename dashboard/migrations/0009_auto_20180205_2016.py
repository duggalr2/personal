# Generated by Django 2.0.1 on 2018-02-05 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20180205_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddetail',
            name='timestamp',
            field=models.TimeField(default=datetime.time(20, 16, 25, 512945)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
