# Generated by Django 4.1.6 on 2023-11-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_store_alter_user_store_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='store',
            field=models.CharField(blank=True, default='FBazaar', max_length=100),
        ),
    ]
