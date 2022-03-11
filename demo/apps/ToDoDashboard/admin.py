from django.contrib import admin
from .models import Member, Dashboard, DashboardColumn, ToDoItem

# Register your models here.
admin.site.register(Member)
admin.site.register(Dashboard)
admin.site.register(DashboardColumn)
admin.site.register(ToDoItem)
