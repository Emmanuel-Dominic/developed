from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    logo = models.ImageField(default='null', blank=True)
    location = models.CharField(max_length=100)
    vision = models.CharField(max_length=255)
