# Generated by Django 4.2.5 on 2023-10-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='delivery_method',
            field=models.CharField(default='Delivery', max_length=50),
        ),
    ]