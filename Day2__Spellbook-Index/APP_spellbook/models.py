from django.db import models

from django.urls import reverse

# Create your models here.
class Spell(models.Model):
    class Elements(models.TextChoices):
        NONE = "No Type"
        FIRE = "Fire"
        WATER = "Water"
        EARTH = "Earth"
        AIR = "Air"
        DARK = "Darkness"
        LIGHT = "Light"

    spell_name = models.CharField(max_length=200)
    spell_mana_cost = models.IntegerField()
    spell_element_type = models.CharField(max_length=50, choices=Elements.choices, default=Elements.NONE)
    spell_ingredients = models.TextField(blank=True, null=True)
    spell_directions = models.TextField(blank=True, null=True)
    spell_is_forbidden = models.BooleanField(default=False)

    def __str__(self):
        return self.spell_name

    def get_absolute_url(self):
        return reverse("home")
