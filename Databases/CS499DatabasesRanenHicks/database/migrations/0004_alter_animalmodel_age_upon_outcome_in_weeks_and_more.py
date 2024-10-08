# Generated by Django 4.1.13 on 2024-08-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0003_animalmodel_outcome_subtype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalmodel",
            name="age_upon_outcome_in_weeks",
            field=models.DecimalField(decimal_places=15, max_digits=100),
        ),
        migrations.AlterField(
            model_name="animalmodel",
            name="date_of_birth",
            field=models.CharField(max_length=100),
        ),
    ]
