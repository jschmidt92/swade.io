from rest_framework.serializers import ModelSerializer
from .models import Cyberware


class CyberwareSerializer(ModelSerializer):
    class Meta:
        model = Cyberware
        fields = "__all__"
