from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    class Type(models.TextChoices):
        BOUNTY = "Bounty"
        DELIVERY = "Delivery"
        SCOUTING_RUN = "Scouting Run"
        NONE = "None"

    class Status(models.TextChoices):
        POSTED = "Posted"
        HIDDEN = "Hidden"
        PUBLIC = "Public and Unclaimed"
        CLAIMED = "Claimed"
        COMPLETED = "Completed"

    title = models.CharField(max_length=250)
    author = models.ForeignKey("User", related_name="created_tasks", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=220)
    task_information = models.TextField((""))
    task_type = models.CharField(max_length=50, choices=Type, default=Type.NONE, null=True, blank=True)
    status = models.CharField(max_length=150, choices=Status.choices, default=Status.HIDDEN)
    claimer = models.ForeignKey(User, related_name="tasks", on_delete=models.PROTECT, null=True, blank=True)
    reward = models.PositiveIntegerField()
    date_created = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ["-date_created"]
        constraints = [
            models.UniqueConstraint(
                fields=["author", "slug", "pk"],
                name="unique_slug_per_author"
            )
        ]


    def get_absolute_url(self):
        return reverse("task_detail_view", kwargs={"username": self.author.username, "slug": self.slug, "pk": self.pk})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    



class Claim(models.Model):
    pass
