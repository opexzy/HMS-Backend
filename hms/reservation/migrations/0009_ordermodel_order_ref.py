# Generated by Django 3.1.2 on 2021-02-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20210218_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='order_ref',
            field=models.CharField(default=' ', max_length=8, unique=True, verbose_name='Order Reference'),
            preserve_default=False,
        ),
    ]
