# Generated by Django 3.1.2 on 2021-02-11 21:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0012_auto_20210209_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 22, 1, 47, 984898, tzinfo=utc), verbose_name='Expires'),
        ),
    ]
