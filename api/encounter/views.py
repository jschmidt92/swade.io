from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Encounter
from .serializers import EncounterSerializer
from character.models import Character
from npc.models import NPC

# Create your views here.
@api_view(["GET"])
def get_all_encounters(request: HttpRequest):
    encounters = Encounter.objects.all()
    serializer = EncounterSerializer(encounters, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_encounter(request: HttpRequest):
    data = request.data
    serializer = EncounterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Success": "The encounter was created successfully"}, status=201
        )
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_encounter(request: HttpRequest, encounter_id: int):
    try:
        encounter = Encounter.objects.get(id=encounter_id)
        serializer = EncounterSerializer(encounter)
        return Response(serializer.data)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)


@api_view(["DELETE"])
def delete_encounter(request: HttpRequest):
    encounter_id = request.data.get("encounter_id")
    try:
        encounter = Encounter.objects.get(id=encounter_id)
        encounter.delete()
        return Response(
            {"Success": "The encounter was deleted successfully"}, status=200
        )
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)


@api_view(["POST"])
def add_character(request: HttpRequest):
    encounter_id = request.data.get("encounter_id")
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    encounter.characters.add(character)
    encounter.save()
    return Response(
        {"Success": "The character was added to the encounter successfully"}
    )


@api_view(["GET"])
def get_characters(request: HttpRequest, encounter_id: int):
    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    serializer = EncounterSerializer(encounter)
    return Response(serializer.data["characters"])


@api_view(["POST"])
def remove_character(request: HttpRequest):
    encounter_id = request.data.get("encounter_id")
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")

    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    encounter.characters.remove(character)

    return Response(
        {"Success": "The character was removed from the encounter successfully"},
        status=200,
    )


@api_view(["POST"])
def add_npc(request: HttpRequest):
    encounter_id = request.data.get("encounter_id")
    npc_id = request.data.get("npc_id")
    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    try:
        npc = NPC.objects.get(id=npc_id)
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)

    encounter.npcs.add(npc)
    encounter.save()
    return Response({"Success": "The npc was added to the encounter successfully"})


@api_view(["GET"])
def get_npcs(request: HttpRequest, encounter_id: int):
    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    serializer = EncounterSerializer(encounter)
    return Response(serializer.data["npcs"])


@api_view(["POST"])
def remove_npc(request: HttpRequest):
    encounter_id = request.data.get("encounter_id")
    npc_id = request.data.get("npc_id")

    try:
        encounter = Encounter.objects.get(id=encounter_id)
    except Encounter.DoesNotExist:
        return Response({"Error": "The encounter does not exist"}, status=404)

    try:
        npc = NPC.objects.get(id=npc_id)
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)

    encounter.npcs.remove(npc)

    return Response(
        {"Success": "The npc was removed from the encounter successfully"},
        status=200,
    )
