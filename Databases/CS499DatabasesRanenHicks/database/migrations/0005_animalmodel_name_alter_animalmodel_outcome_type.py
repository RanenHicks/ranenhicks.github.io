# Generated by Django 4.1.13 on 2024-08-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0004_alter_animalmodel_age_upon_outcome_in_weeks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animalmodel",
            name="name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="animalmodel",
            name="outcome_type",
            field=models.CharField(default="No Name", max_length=100),
        ),
    ]
