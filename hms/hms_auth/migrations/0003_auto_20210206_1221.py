# Generated by Django 3.1.2 on 2021-02-06 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0002_auto_20210206_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 11, 36, 1, 987033, tzinfo=utc), verbose_name='Expires'),
        ),
    ]
