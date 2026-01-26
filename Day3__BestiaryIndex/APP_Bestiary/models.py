from django.db import models

# Create your models here.
class Beast(models.Model):
    class Locations(models.Choices):
        NEBULA_FOREST = "Nebula Forest"
        GREEN_PLAINS = "Green Plains"
        RED_DESERT = "Red Desert"
        ABYSSAL_OCEAN = "Abyssal Ocean"
        UNKNOWN = "Unknown"

    class Threats(models.TextChoices):
        EASY = "1_EASY", "Easy"
        MEDIUM = "2_MEDIUM", "Medium"
        HARD = "3_HARD", "Hard"
        EXTRA_HARD = "4_EXTRA_HARD", "Extra Hard"
        MEGA_HARD = "5_MEGA_HARD", "Mega Hard"
        DEATH = "6_DEATHLY_HARD", "Deathly Hard"

    name = models.CharField(max_length=50)
    attack_power = models.PositiveIntegerField(default=1)
    attack_speed = models.PositiveIntegerField(default=1)
    defense = models.PositiveIntegerField(default=1)
    found = models.CharField(max_length=50, choices=Locations.choices, default=Locations.UNKNOWN)
    threat_level = models.CharField(max_length=50, choices=Threats.choices, default=Threats.EASY)
    is_legendary = models.BooleanField(default=False)
    notable_attack = models.TextField()
    quirky_behavior = models.TextField()

    def __str__(self):
        return self.name
