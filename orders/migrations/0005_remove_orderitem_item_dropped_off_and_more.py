# Generated by Django 4.2.5 on 2023-10-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_drop_off_location_orderitem_drop_off_location_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_dropped_off',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_pick_up_status',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_picked_up_status',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Picked Up', 'Picked Up'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], default='Pending', max_length=70),
        ),
    ]