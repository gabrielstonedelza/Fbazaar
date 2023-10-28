# Generated by Django 4.2.5 on 2023-10-28 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0007_orderitem_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='assigned_driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='driver_assigned_to_deliver_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
