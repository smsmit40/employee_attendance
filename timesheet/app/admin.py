from django.contrib import admin
from .models import Employee, TimeEntry, Project
# Register your models here.

admin.site.register(Employee)
admin.site.register(TimeEntry)
admin.site.register(Project)