# Generated by Django 4.1.4 on 2022-12-18 08:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Guardian",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idn", models.IntegerField(blank=True, null=True, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=64, null=True)),
                ("last_name", models.CharField(blank=True, max_length=64, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.PositiveSmallIntegerField(
                        choices=[
                            ("", "Select"),
                            (1, "Male"),
                            (2, "Female"),
                            (3, "Other"),
                        ],
                        default=1,
                    ),
                ),
                ("job", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=16,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?1?\\d{8,15}$"
                            )
                        ],
                    ),
                ),
                ("add", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Orphan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idn", models.IntegerField(unique=True)),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                (
                    "gender",
                    models.PositiveSmallIntegerField(
                        choices=[
                            ("", "Select"),
                            (1, "Male"),
                            (2, "Female"),
                            (3, "Other"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "dental_img",
                    models.ImageField(blank=True, null=True, upload_to=None),
                ),
                ("est_age", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[("", "Select"), (1, "Not adopted"), (2, "Adopted")],
                        default=1,
                    ),
                ),
                (
                    "guardian_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orphanage.guardian",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Outing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_out", models.DateField(default=django.utils.timezone.now)),
                ("time_out", models.TimeField(default=django.utils.timezone.now)),
                ("reason", models.TextField()),
                ("accompany_first_name", models.CharField(max_length=64)),
                ("accompany_last_name", models.CharField(max_length=64)),
                ("accompany_idn", models.IntegerField()),
                (
                    "accompany_phone",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?1?\\d{8,15}$"
                            )
                        ],
                    ),
                ),
                ("date_in", models.DateField(blank=True, null=True)),
                ("time_in", models.TimeField(blank=True, null=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            ("", "Select"),
                            (1, "Outing"),
                            (2, "On-time"),
                            (3, "Delay"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "orphan_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orphanage.orphan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Adoption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idn", models.IntegerField(unique=True)),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("dob", models.DateField()),
                (
                    "gender",
                    models.PositiveSmallIntegerField(
                        choices=[
                            ("", "Select"),
                            (1, "Male"),
                            (2, "Female"),
                            (3, "Other"),
                        ],
                        default=1,
                    ),
                ),
                ("job", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone",
                    models.CharField(
                        max_length=16,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?1?\\d{8,15}$"
                            )
                        ],
                    ),
                ),
                ("add", models.TextField()),
                (
                    "orphan_fk",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orphanage.orphan",
                    ),
                ),
            ],
        ),
    ]