from django.contrib.auth import models
from django.utils import timezone


class DiscordUserOAuth2Manager(models.UserManager):
    def create_new_discord_user(self, user):
        new_user = self.create(
            id=user["id"],
            username=user["username"],
            global_name=user["global_name"],
            avatar=user["avatar"],
            mfa_enabled=user["mfa_enabled"],
            locale=user["locale"],
            email=user["email"],
            verified=user["verified"],
            date_joined=timezone.now()
        )
        return new_user
