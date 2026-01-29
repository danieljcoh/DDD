from django.db import models

# Create your models here.
class Character(models.Model):
    player_name = models.CharField(max_length=200)
    player_character_name = models.CharField(max_length=200)
    party = models.ForeignKey("Party", null=True, blank=True, on_delete=models.SET_NULL)


class Party(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField(default=1)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Creature(models.Model):
    name = models.CharField(max_length=50)
    threat_points = models.PositiveIntegerField(default=1) # the higher the number, the harder the difficulty?

    def __str__(self):
        return self.name
    

class Encounter(models.Model):
    encounter_name = models.CharField(max_length=200)
    party = models.ForeignKey("Party", on_delete=models.CASCADE)

    def __str__(self):
        return self.encounter_name
    
    def total_treat(self):
        return sum(entry.creature.threat_points * entry.quantity for entry in self.entries.all())
    

class EncounterEntry(models.Model):
    encounter = models.ForeignKey("Encounter", related_name="entries", on_delete=models.CASCADE)
    creature = models.ForeignKey("Creature", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.creature} x{self.quantity}"