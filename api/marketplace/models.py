from django.db import models

# Create your models here.
class Transaction(models.Model):
    character = models.ForeignKey('character.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=25)
    item_type = models.CharField(max_length=25, blank=True)
    item_id = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    transaction_time = models.DateTimeField(auto_now_add=True)
