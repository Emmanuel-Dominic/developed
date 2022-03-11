from django.db import models

from demo.apps.users.models import User
from .utils import *

# Create your models here.
class CoffeeStore(models.Model):
    name = models.CharField(max_length=10, choices=COFFEE_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    quantity = models.CharField(max_length=1, choices=QUANTITY_CHOICES)

    def __str__(self):
        return self.name


class CoffeeOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=COFFEE_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    quantity = models.CharField(max_length=1, choices=QUANTITY_CHOICES)

    def __str__(self):
        return self.name
