from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer

# Create your views here.
@api_view(["GET"])
def get_all_characters(request: HttpRequest):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_character(request: HttpRequest):
    data = request.data
    serializer = CharacterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Success": "The character was created successfully"}, status=201
        )
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_character(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)


@api_view(["GET"])
def get_character_by_id(request: HttpRequest, id: int):
    try:
        character = Character.objects.get(id=id)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)


@api_view(["GET"])
def list_characters(request: HttpRequest, discord_id: int):
    characters = Character.objects.filter(discordID=discord_id)
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_character(request: HttpRequest, id: int):
    try:
        character = Character.objects.get(id=id)
        character.delete()
        return Response(
            {"Success": "The character was deleted successfully"}, status=200
        )
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)


@api_view(["GET"])
def get_money(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
        return Response({"money": character.money})
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)


@api_view(["POST"])
def add_money(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    amount = request.data.get("amount")
    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
        character.money += int(amount)
        character.save()
        return Response(
            {
                "Success": f"Added ${amount} to {character.name}",
                "Total Money": character.money,
            }
        )
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)


@api_view(["POST"])
def remove_money(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    amount = request.data.get("amount")
    try:
        character = Character.objects.get(discordID=discord_id, name=character_name)
        if character.money >= int(amount):
            character.money -= int(amount)
            character.save()
            return Response(
                {
                    "Success": f"Removed {amount} from {character.name}",
                    "Total Money": character.money,
                }
            )
        else:
            return Response({"Error": "Not enough money"}, status=400)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)
