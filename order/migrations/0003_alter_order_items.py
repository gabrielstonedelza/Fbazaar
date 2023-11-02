# Generated by Django 4.2.5 on 2023-11-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='orders', to='orders.orderitem'),
        ),
    ]