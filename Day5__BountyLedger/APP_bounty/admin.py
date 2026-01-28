from django.contrib import admin

from .models import Outlaw, Bounty

# Register your models here.

class BountyAdmin(admin.ModelAdmin):
    list_display = "title", "description", "reward_amount", "rewarded_to"


class OutlawAdmin(admin.ModelAdmin):
    list_display = "player_name", "player_character_name"
    ordering = ["player_name"]


admin.site.register(Bounty, BountyAdmin)
admin.site.register(Outlaw, OutlawAdmin)