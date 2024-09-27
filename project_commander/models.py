from django.db import models
from django.contrib.auth.models import User


TYPE = ((0, "Item"), (1, "List"))
PRIORITY = ((0, "Select Priority"), (1, "Needed"), (2, "Will need soon"), (3, "Would be nice to have"), (4, "It can wait"))


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category_type = models.IntegerField(choices=TYPE, default=0)


class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    item_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category", default=0
    )
    min_quantity = models.IntegerField(default=0, blank=True)
    current_quantity = models.IntegerField(default=0, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0, blank=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    class Meta:
        ordering = ["priority"]


class List(models.Model):
    list_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    list_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="list_category", default=0
    )