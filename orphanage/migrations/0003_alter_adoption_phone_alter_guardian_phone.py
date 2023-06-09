# Generated by Django 4.1.4 on 2022-12-28 16:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("orphanage", "0002_rename_phone_number_guardian_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adoption",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=16, region=None, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="guardian",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=16, region=None, unique=True
            ),
        ),
    ]
