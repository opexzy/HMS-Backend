# Generated by Django 3.1.2 on 2021-02-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodordermodel',
            name='completed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='food_order_completed_by', to='staff.staffmodel', verbose_name='Commpleted By'),
        ),
    ]