# Generated by Django 5.0.3 on 2024-03-18 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="graduation_year",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1970),
                    django.core.validators.MaxValueValidator(2024),
                ]
            ),
        ),
    ]