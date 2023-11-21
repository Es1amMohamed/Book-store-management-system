from django.db import models

# Create your models here.


class Book(models.Model):
    status_choices = (
        ("available", "Available"),
        ("rented", "Rented"),
        ("sold", "Sold"),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_image = models.ImageField(
        upload_to="image_books/",
        default="image_books/default.png",
        null=True,
        blank=True,
    )
    author_image = models.ImageField(
        upload_to="image_authors/",
        default="image_authors/default.png",
        null=True,
        blank=True,
    )
    pages = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_price_day = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    rental_period = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50, choices=status_choices, default="available"
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
