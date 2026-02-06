from django.db import models


# Create your models here.
class Character(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    player_character_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.player_character_name}: ({self.first_name} {self.last_name})"
    

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    owner = models.ForeignKey("Character", related_name="items", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.item_name}"


class TransferLog(models.Model):
    transfer_from = models.ForeignKey("Character", related_name="transfers", on_delete=models.PROTECT, null=True, blank=True) #protect where items have been if characters are deleted.
    transfer_to = models.ForeignKey("Character", on_delete=models.PROTECT, null=True, blank=True)
    item_transferred = models.ForeignKey("Item", on_delete=models.PROTECT)
    transfer_created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)


    # ADD VALIDATION IF THE ITEM EVEN BELONGS TO THE PERSON and then it removes the item
    def can_transfer(self):
        pass

    def transfer_set_name(self):
        return f"{self.item_transferred} was transferred to {self.transfer_to} from {self.transfer_from}."
    
    def __str__(self):
        return self.transfer_set_name()
    
    class Meta:
        ordering = ["-transfer_created_at"]