# Generated by Django 4.1.4 on 2022-12-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donation", "0002_alter_cashdonation_amt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cashdonation",
            name="status",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    ("", "Select"),
                    (1, "Unreceived"),
                    (2, "Pending"),
                    (3, "Received"),
                ],
                default=2,
            ),
        ),
    ]
