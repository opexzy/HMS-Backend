# Generated by Django 3.1.2 on 2021-02-20 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hms_auth', '0029_auto_20210220_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 12, 54, 48, 936372, tzinfo=utc), verbose_name='Expires'),
        ),
    ]
