# Generated by Django 5.2 on 2025-04-26 23:30

import localflavor.mx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.mx.models.MXStateField(default='DF', max_length=4),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
