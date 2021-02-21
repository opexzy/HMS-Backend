# Generated by Django 3.1.2 on 2021-02-19 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0009_ordermodel_order_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Coupon Id')),
                ('code', models.CharField(max_length=14, unique=True, verbose_name='Coupon Code')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Coupon Discount')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.reservationmodel', verbose_name='Reservation')),
            ],
            options={
                'db_table': 'hms_coupon',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
