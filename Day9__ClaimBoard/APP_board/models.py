from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    class Type(models.TextChoices):
        BOUNTY = "Bounty", "Bounty"
        DELIVERY = "Delivery", "Delivery"
        SCOUTING_RUN = "Scouting Run", "Scouting Run"
        NONE = "None", "None"

    class Status(models.TextChoices):
        DRAFT = "Draft", "Draft"
        POSTED = "Posted", "Posted"
        CLAIMED = "Claimed", "Claimed"
        COMPLETED = "Completed", "Completed"

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="created_tasks", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=220, unique=True)
    task_information = models.TextField((""))
    task_type = models.CharField(max_length=50, choices=Type, default=Type.NONE, null=True, blank=True)
    status = models.CharField(max_length=150, choices=Status.choices, default=Status.DRAFT)
    claimer = models.ForeignKey(User, related_name="tasks", on_delete=models.PROTECT, null=True, blank=True)
    reward = models.PositiveIntegerField()
    date_created = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ["-date_created"]


    def get_absolute_url(self):
        return reverse("task_detail_view", kwargs={"username": self.author.username, "slug": self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            n = 1
            while Task.objects.filter(slug=slug).exists():
                n += 1
                slug = f"{base}-{n}"
            self.slug = slug
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    



class Claim(models.Model):
    claimer = models.ForeignKey(User, related_name="claimers", on_delete=models.PROTECT)
    task = models.ForeignKey("Task", related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["claimer", "task"],
                name="one_claimer_per_task"
            )
        ]

    def __str__(self):
        return f"{self.claimer} claimed {self.task}."