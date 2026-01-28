from django.db import models

# Create your models here.
class Bounty(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() # there needs to be logic to add this to the Outlaw's total_gold somehow. 
    reward_amount = models.PositiveIntegerField(default=0)
    rewarded_to = models.ForeignKey("Outlaw", related_name="bounties", on_delete=models.PROTECT, blank=True, null=True) #even if the person would die, people would know who complete it. #if this is full, it's completed.

    def __str__(self):
        return self.title


class Outlaw(models.Model):
    player_name = models.CharField(max_length=200)
    player_character_name = models.CharField(max_length=200)
    total_gold = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player_name} playing as {self.player_character_name}."