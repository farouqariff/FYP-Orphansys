# Generated by Django 4.1.4 on 2023-01-20 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orphanage", "0012_alter_outing_time_out"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outing",
            name="time_out",
            field=models.TimeField(default=datetime.time(10, 16, 47, 702321)),
        ),
    ]
