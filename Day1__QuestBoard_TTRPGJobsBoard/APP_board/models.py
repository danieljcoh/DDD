from django.db import models

# Create your models here.
class Quest(models.Model):
    class Difficulties(models.TextChoices):
        EASY = "Easy", "EZ"
        MED = "Medium", "MED"
        HARD = "Hard", "HD"

    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    difficulty = models.CharField(max_length=20, choices=Difficulties.choices, default=Difficulties.EASY)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    reward = models.IntegerField()
    open_or_closed = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:20]
    
    class Meta:
        ordering = ['-created_on']