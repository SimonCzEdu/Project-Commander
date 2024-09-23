from django.db import models
from django.contrib.auth.models import User

TYPE = ((0, "Item"), (1, "List"))


# Create your models here.
class Categorie(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category_type = models.IntegerField(choices=TYPE, default=0)