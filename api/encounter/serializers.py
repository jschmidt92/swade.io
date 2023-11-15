from rest_framework.serializers import ModelSerializer
from .models import Encounter
from character.models import Character
from npc.models import NPC


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ["name", "damage"]


class NPCSerializer(ModelSerializer):
    class Meta:
        model = NPC
        fields = ["name", "damage", "faction"]


class EncounterSerializer(ModelSerializer):
    characters = CharacterSerializer(many=True, required=False)
    npcs = NPCSerializer(many=True, required=False)

    class Meta:
        model = Encounter
        fields = ["id", "name", "notes", "body", "characters", "npcs"]

    def create(self, validated_data):
        characters_data = validated_data.pop("characters", [])
        npcs_data = validated_data.pop("npcs", [])

        encounter = Encounter.objects.create(**validated_data)

        for character_data in characters_data:
            character = Character.objects.get(id=character_data["id"])
            encounter.characters.add(character)

        for npc_data in npcs_data:
            npc = NPC.objects.get(id=npc_data["id"])
            encounter.npcs.add(npc)

        return encounter
