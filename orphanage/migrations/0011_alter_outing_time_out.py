# Generated by Django 4.1.4 on 2022-12-30 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orphanage", "0010_alter_outing_time_out"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outing",
            name="time_out",
            field=models.TimeField(default=datetime.time(19, 6, 3, 521244)),
        ),
    ]
