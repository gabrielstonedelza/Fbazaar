# Generated by Django 4.2.5 on 2023-10-21 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='itemremarks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_making_remarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemratings',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_api.storeitem'),
        ),
        migrations.AddField(
            model_name='itemratings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addtopricechanged',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_api.storeitem'),
        ),
    ]
