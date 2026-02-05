from django.contrib import admin

from .models import *

# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["player_character_name", "first_name", "last_name"]


class ItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "owner"]


admin.site.register(Character, CharacterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(TransferLog)