# Generated by Django 3.1.2 on 2021-03-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_bookingrecordmodel_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='category',
            field=models.CharField(default='room', max_length=25, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
