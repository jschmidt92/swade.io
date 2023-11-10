from django.db import models

# Create your models here.
class Cyberware(models.Model):
    name = models.CharField(max_length=255)
    strain = models.IntegerField()
    effect = models.TextField(blank=True)
    price = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
