# Generated by Django 4.2.5 on 2023-10-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0006_rename_store_itemratings_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='exclusive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='storeitem',
            name='promotion',
            field=models.BooleanField(default=False),
        ),
    ]