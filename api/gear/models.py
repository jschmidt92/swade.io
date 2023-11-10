from django.db import models

# Create your models here.
class Gear(models.Model):
    name = models.CharField(max_length=255)
    min_str = models.CharField(max_length=255)
    wt = models.IntegerField()
    price = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name