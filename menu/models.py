import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __float__(self):
        return self.price

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)