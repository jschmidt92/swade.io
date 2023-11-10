from rest_framework.serializers import ModelSerializer
from .models import Weapon


class WeaponSerializer(ModelSerializer):
    class Meta:
        model = Weapon
        fields = "__all__"
