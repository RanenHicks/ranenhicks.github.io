# Generated by Django 4.1.13 on 2024-08-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0002_animalmodel_delete_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="animalmodel",
            name="outcome_subtype",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
