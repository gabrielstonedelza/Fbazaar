# Generated by Django 4.1.6 on 2023-11-10 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordering_item', to='orders.orderitem'),
        ),
    ]
