# Generated by Django 3.1.2 on 2021-02-19 10:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0024_auto_20210219_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 10, 51, 35, 363714, tzinfo=utc), verbose_name='Expires'),
        ),
    ]
