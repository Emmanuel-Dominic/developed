from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    bio = models.TextField()
    active = models.BooleanField(default=False)

# class Worker(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="companies")
#     name = models.CharField(max_length=25)
#     date_joined = models.DateField(auto_now=True)
