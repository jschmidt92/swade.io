from django.db import models

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=255)
    range = models.CharField(max_length=255, blank=True)
    damage = models.CharField(max_length=255)
    rof = models.IntegerField(default=0)
    shots = models.IntegerField(default=0)
    min_str = models.CharField(max_length=255, blank=True)
    wt = models.IntegerField()
    price = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name