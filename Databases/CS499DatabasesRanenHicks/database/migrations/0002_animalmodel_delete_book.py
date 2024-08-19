# Generated by Django 5.1 on 2024-08-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnimalModel",
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
                ("age_upon_outcome", models.CharField(max_length=100)),
                ("animal_id", models.CharField(max_length=100)),
                ("animal_type", models.CharField(max_length=100)),
                ("breed", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("datetime", models.CharField(max_length=100)),
                ("mothyear", models.CharField(max_length=100)),
                ("outcome_type", models.CharField(max_length=100)),
                ("sex_upon_outcome", models.CharField(max_length=100)),
                ("location_lat", models.DecimalField(decimal_places=2, max_digits=100)),
                (
                    "location_long",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
                (
                    "age_upon_outcome_in_weeks",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
