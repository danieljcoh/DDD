from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=1)
    quantity_available = models.IntegerField(default=1)
    holder = models.ForeignKey("Character", null=True, blank=True, related_name="items", on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}."


class Character(models.Model):
    player_character_name = models.CharField(max_length=200)
    player_name = models.CharField(max_length=200)

    def __str__(self):
        return self.player_character_name
    