# Generated by Django 4.2.5 on 2023-10-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0005_alter_storeitem_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemratings',
            old_name='store',
            new_name='item',
        ),
    ]