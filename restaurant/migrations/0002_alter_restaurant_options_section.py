# Generated by Django 5.1.6 on 2025-04-01 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="restaurant",
            options={"verbose_name": "Ресторан", "verbose_name_plural": "Ресторан"},
        ),
        migrations.CreateModel(
            name="Section",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название секции"),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="restaurant.restaurant",
                        verbose_name="Ресторан",
                    ),
                ),
            ],
            options={
                "verbose_name": "Секция",
                "verbose_name_plural": "Секции",
                "indexes": [
                    models.Index(
                        fields=["restaurant", "name"],
                        name="restaurant__restaur_7d43bc_idx",
                    )
                ],
                "unique_together": {("restaurant", "name")},
            },
        ),
    ]
