# Generated by Django 4.2.5 on 2023-11-21 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("author", models.CharField(max_length=100)),
                (
                    "book_image",
                    models.ImageField(blank=True, null=True, upload_to="image_books/"),
                ),
                (
                    "author_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="image_authors/"
                    ),
                ),
                ("pages", models.IntegerField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "rental_price_day",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("rental_period", models.IntegerField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("rented", "Rented"),
                            ("sold", "Sold"),
                        ],
                        default="available",
                        max_length=50,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.category",
                    ),
                ),
            ],
        ),
    ]
