# Generated by Django 4.1.7 on 2023-07-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_hazard_benefit"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="media/")),
            ],
        ),
    ]
