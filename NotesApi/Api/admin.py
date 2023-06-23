from django.contrib import admin
from .models import *

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'audio', 'video']
