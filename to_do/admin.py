from django.contrib import admin
from .models import ToDoModel



@admin.register(ToDoModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = []