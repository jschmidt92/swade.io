from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cyberware
from .serializers import CyberwareSerializer
from character.models import *

# Create your views here.
@api_view(["GET"])
def get_all_cyberware(request: HttpRequest):
    cyberware = Cyberware.objects.all()
    serializer = CyberwareSerializer(cyberware, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_cyberware(request: HttpRequest):
    data = request.data
    serializer = CyberwareSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Success": "The cyberware was created successfully"}, status=201
        )
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_cyberware(request: HttpRequest, cyberware_id: int):
    try:
        cyberware = Cyberware.objects.get(id=cyberware_id)
        serializer = CyberwareSerializer(cyberware)
        return Response(serializer.data)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)


@api_view(["GET"])
def get_cyberware_by_name(request: HttpRequest):
    cyberware_name = request.data.get("cyberware_name")
    try:
        cyberware = Cyberware.objects.get(name=cyberware_name)
        serializer = CyberwareSerializer(cyberware)
        return Response(serializer.data)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)


@api_view(["DELETE"])
def delete_cyberware(request: HttpRequest, cyberware_id: int):
    try:
        cyberware = Cyberware.objects.get(id=cyberware_id)
        cyberware.delete()
        return Response(
            {"Success": "The cyberware was deleted successfully"}, status=200
        )
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)


@api_view(["POST"])
def add_cyberware(request: HttpRequest):
    character_id = request.data.get("character_id")
    cyberware_id = request.data.get("cyberware_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        cyberware = Cyberware.objects.get(id=cyberware_id)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)

    character.cyberware.add(cyberware)

    return Response(
        {"Success": "The cyberware was added to the character successfully"}, status=201
    )


@api_view(["POST"])
def remove_cyberware(request: HttpRequest):
    character_id = request.data.get("character_id")
    cyberware_id = request.data.get("cyberware_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        cyberware = Cyberware.objects.get(id=cyberware_id)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)

    character.cyberware.remove(cyberware)

    return Response(
        {"Success": "The cyberware was removed from the character successfully"},
        status=200,
    )


@api_view(["POST"])
def buy_cyberware(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    cyberware_name = request.data.get("cyberware_name")

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        cyberware = Cyberware.objects.get(name=cyberware_name)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)

    if character.buy_cyberware(cyberware):
        return Response(
            {"Success": "The cyberware was bought successfully"}, status=200
        )
    else:
        return Response({"Error": "Not enough money"}, status=400)


@api_view(["POST"])
def sell_cyberware(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    cyberware_name = request.data.get("cyberware_name")

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        cyberware = Cyberware.objects.get(name=cyberware_name)
    except Cyberware.DoesNotExist:
        return Response({"Error": "The cyberware does not exist"}, status=404)

    if character.sell_cyberware(cyberware):
        return Response({"Success": "The cyberware was sold successfully"}, status=200)
    else:
        return Response(
            {"Error": "The character does not have the cyberware"}, status=400
        )
