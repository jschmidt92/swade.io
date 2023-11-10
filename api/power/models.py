from django.db import models

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=255)
    pp = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    effect = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name