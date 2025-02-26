from django.contrib import admin
from .models import ToDoModel
from parler.admin import TranslatableAdmin



@admin.register(ToDoModel)
class ToDoAdmin(TranslatableAdmin):
    list_display = []