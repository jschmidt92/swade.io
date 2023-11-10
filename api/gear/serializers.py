from rest_framework.serializers import ModelSerializer
from .models import Gear


class GearSerializer(ModelSerializer):
    class Meta:
        model = Gear
        fields = "__all__"
