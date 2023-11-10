from rest_framework.serializers import IntegerField, ModelSerializer
from .models import NPC, GearQuantity, WeaponQuantity
from cyberware.models import Cyberware
from gear.models import Gear
from power.models import Power
from weapon.models import Weapon


class CyberwareSerializer(ModelSerializer):
    class Meta:
        model = Cyberware
        fields = "__all__"


class GearSerializer(ModelSerializer):
    class Meta:
        model = Gear
        fields = "__all__"


class PowerSerializer(ModelSerializer):
    class Meta:
        model = Power
        fields = "__all__"


class WeaponSerializer(ModelSerializer):
    class Meta:
        model = Weapon
        fields = "__all__"


class GearQuantitySerializer(ModelSerializer):
    gear = GearSerializer()

    class Meta:
        model = GearQuantity
        fields = ["gear", "quantity"]


class WeaponQuantitySerializer(ModelSerializer):
    weapon = WeaponSerializer()

    class Meta:
        model = WeaponQuantity
        fields = ["weapon", "quantity"]


class NPCSerializer(ModelSerializer):
    ammo = IntegerField(required=False)
    cyberware = CyberwareSerializer(many=True, required=False)
    gear = GearQuantitySerializer(source="gearquantity_set", many=True, required=False)
    money = IntegerField(required=False)
    powers = PowerSerializer(many=True, required=False)
    weapons = WeaponQuantitySerializer(
        source="weaponquantity_set", many=True, required=False
    )

    class Meta:
        model = NPC
        fields = [
            "id",
            "name",
            "race",
            "gender",
            "charisma",
            "pace",
            "parry",
            "toughness",
            "attributes",
            "skills",
            "hindrances",
            "edges",
            "cyberware",
            "powers",
            "gear",
            "weapons",
            "damage",
            "ammo",
            "money",
        ]

    def create(self, validated_data):
        gear_data = validated_data.pop("gear", [])
        weapons_data = validated_data.pop("weapons", [])

        npc = NPC.objects.create(**validated_data)

        for gear_data_item in gear_data:
            GearQuantity.objects.create(npc=npc, **gear_data_item)

        for weapon_data_item in weapons_data:
            WeaponQuantity.objects.create(npc=npc, **weapon_data_item)

        return npc
