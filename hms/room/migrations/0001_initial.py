# Generated by Django 3.1.2 on 2021-02-08 13:32

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0004_auto_20210206_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Reservation Id')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Room')),
                ('Description', models.CharField(max_length=255, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Room Price')),
                ('start_no', models.IntegerField(verbose_name='Room Start No')),
                ('end_no', models.IntegerField(verbose_name='Room End No')),
                ('available', models.IntegerField(verbose_name='Available Room')),
            ],
            options={
                'db_table': 'hms_room',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BookingRecordModel',
            fields=[
                ('timestamp', models.DateTimeField(auto_created=True, verbose_name='Timestamp')),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Reservation Id')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Amount')),
                ('qauntity', models.IntegerField(verbose_name='Quantity')),
                ('check_in', models.DateField(verbose_name='Checkin Date')),
                ('check_out', models.DateField(verbose_name='Checkout Date')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.reservationmodel', verbose_name='Reservation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='room.roommodel', verbose_name='Room')),
            ],
            options={
                'db_table': 'hms_booking_record',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]