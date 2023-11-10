from django.db import models
from .managers import DiscordUserOAuth2Manager


# Create your models here.
class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    global_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True)
    mfa_enabled = models.BooleanField()
    locale = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    verified = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)
    is_gm = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def is_authenticated(self, request):
        return True
