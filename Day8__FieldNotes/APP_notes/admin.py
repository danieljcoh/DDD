from django.contrib import admin

from .models import FieldNote

# Register your models here.


class FieldNoteAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]


admin.site.register(FieldNote, FieldNoteAdmin)