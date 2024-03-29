# Generated by Django 3.1.2 on 2021-02-09 20:42

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('reservation', '0004_auto_20210206_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Drink Id')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Food Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Drink Price')),
                ('metric', models.CharField(max_length=255, verbose_name='Metric')),
                ('available', models.IntegerField(verbose_name='Available Drink')),
            ],
            options={
                'db_table': 'hms_drink',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DrinkOrderModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Reservation Id')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Amount')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('status', models.CharField(max_length=15, verbose_name='Status')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bar.drinkmodel', verbose_name='Drink')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.staffmodel', verbose_name='Registered By')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.reservationmodel', verbose_name='Reservation')),
            ],
            options={
                'db_table': 'hms_drink_order',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
