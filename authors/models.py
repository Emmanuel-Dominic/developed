from unicodedata import name
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    active = models.BooleanField(default=False)
