from django.db import models
from django.conf import settings


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='photos/', blank=True)
    department = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='LAST UPDATE')


class Dashboard(models.Model):
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member')
    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class DashboardColumn(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class ToDoItem(models.Model):
    dashboard_column = models.ForeignKey(DashboardColumn, on_delete=models.CASCADE)
    subtask_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    label = models.CharField(max_length=128, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    time_estimate_hours = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'
