# Generated by Django 3.1.2 on 2021-02-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionmodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Option Name'),
        ),
    ]
