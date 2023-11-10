from rest_framework.serializers import ModelSerializer
from .models import Power


class PowerSerializer(ModelSerializer):
    class Meta:
        model = Power
        fields = "__all__"
