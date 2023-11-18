from django.db import models
from discordlogin.models import DiscordUser


# Create your models here.
class Event(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    details = models.TextField()
    attendance = models.JSONField(default=dict)
