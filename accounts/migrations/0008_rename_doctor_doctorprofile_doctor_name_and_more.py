# Generated by Django 5.0.3 on 2024-03-19 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_doctorprofile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctorprofile",
            old_name="doctor",
            new_name="doctor_name",
        ),
        migrations.CreateModel(
            name="PharmacistProfile",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "pharmacist_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.pharmacist",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pharmacist Profile",
                "verbose_name_plural": "Pharmacists Profiles",
                "ordering": ["-created_at"],
            },
        ),
    ]