# Generated by Django 4.2.5 on 2023-10-31 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0002_initial'),
        ('orders', '0009_remove_clearedpickups_order_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_api.storeitem'),
        ),
    ]
