from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class FieldNote(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    information_text = models.TextField()
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    author = models.ForeignKey(User, related_name=("field_notes"), on_delete=models.PROTECT) # we protect to know who created the note even if a researcher dies or goes missing

    def __str__(self):
        return f"{self.title}"

# class ResearchScout(models.Model):
#     first_name = models.CharField(max_length=300)
#     last_name = models.CharField(max_length=300)
#     age = models.PositiveIntegerField(default=13)

class Confirmation(models.Model):
    scout = models.ManyToManyField(User)
    field_note = models.ManyToManyField("FieldNote")