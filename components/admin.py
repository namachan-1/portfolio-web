from django.contrib import admin
from .models import Project


# A class that allows modification within the Django admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


# Registers the given model as an admin
admin.site.register(Project, ProjectAdmin)
