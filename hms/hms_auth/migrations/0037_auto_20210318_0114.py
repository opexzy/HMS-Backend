# Generated by Django 3.1.2 on 2021-03-18 00:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0036_auto_20210224_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 0, 29, 37, 895471, tzinfo=utc), verbose_name='Expires'),
        ),
    ]