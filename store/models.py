from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.TextChoices):
    CLOTHES = 'clothes'
    JEWELLERY = 'Jewellery'


class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.CharField(choices=Category.choices , max_length=100)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    addedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    addAt = models.DateTimeField(auto_now_add=True)
    brandName = models.CharField(max_length=100)

