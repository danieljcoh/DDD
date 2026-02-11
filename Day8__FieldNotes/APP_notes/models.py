from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class FieldNote(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    information_text = models.TextField()
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    author = models.ForeignKey(User, related_name="field_notes", on_delete=models.PROTECT) # we protect to know who created the note even if a researcher dies or goes missing
    slug = models.SlugField(max_length=220)
    is_public = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "slug"],
                name="unique_slug_per_author"
            )
        ]

    def get_absolute_url(self):
        return reverse("fieldnotes_detail_view", kwargs={"username": self.author.username, "slug":self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Confirmation(models.Model):
    scout = models.ForeignKey(User, on_delete=models.CASCADE, related_name="confirmations")
    field_note = models.ForeignKey("FieldNote", related_name="confirmations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["scout", "field_note"],
                name="unique_confimration_per_scount_per_note"
            )
        ]
    
    def __str__(self):
        return f"{self.scout.username} confirmed {self.field_note.slug}"