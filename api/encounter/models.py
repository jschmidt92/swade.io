from django.db import models
from character.models import Character
from npc.models import NPC

# Create your models here.
class Encounter(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    body = models.TextField(blank=True)
    characters = models.ManyToManyField(Character, blank=True)
    npcs = models.ManyToManyField(NPC, blank=True)

    def __str__(self):
        return self.name
