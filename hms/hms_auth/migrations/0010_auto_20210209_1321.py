# Generated by Django 3.1.2 on 2021-02-09 12:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0009_auto_20210209_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 12, 35, 45, 275193, tzinfo=utc), verbose_name='Expires'),
        ),
    ]
