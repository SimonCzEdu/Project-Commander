# Generated by Django 4.2.16 on 2024-09-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categorie",
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
                ("category_name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "category_type",
                    models.IntegerField(choices=[(0, "Item"), (1, "List")], default=0),
                ),
            ],
        ),
    ]
