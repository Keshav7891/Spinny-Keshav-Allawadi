# Generated by Django 4.2.4 on 2023-08-31 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_box_createdby_box_area_box_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='box',
            name='updatedOn',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
