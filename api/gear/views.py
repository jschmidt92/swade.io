from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gear
from .serializers import GearSerializer
from character.models import *

# Create your views here.
@api_view(["GET"])
def get_all_gear(request: HttpRequest):
    gear = Gear.objects.all()
    serializer = GearSerializer(gear, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_gear(request: HttpRequest):
    data = request.data
    serializer = GearSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The gear was created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_gear(request: HttpRequest, gear_id: int):
    try:
        gear = Gear.objects.get(id=gear_id)
        serializer = GearSerializer(gear)
        return Response(serializer.data)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)


@api_view(["GET"])
def get_gear_by_name(request: HttpRequest):
    gear_name = request.data.get("gear_name")
    try:
        gear = Gear.objects.get(name=gear_name)
        serializer = GearSerializer(gear)
        return Response(serializer.data)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)


@api_view(["DELETE"])
def delete_gear(request: HttpRequest, gear_id: int):
    try:
        gear = Gear.objects.get(id=gear_id)
        gear.delete()
        return Response({"Success": "The gear was deleted successfully"}, status=200)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)


@api_view(["POST"])
def add_gear(request: HttpRequest):
    character_id = request.data.get("character_id")
    gear_id = request.data.get("gear_id")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        gear = Gear.objects.get(id=gear_id)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)

    gear_quantity, created = GearQuantity.objects.get_or_create(
        character=character, gear=gear, defaults={"quantity": quantity}
    )
    if not created:
        gear_quantity.quantity += quantity
        gear_quantity.save()

    return Response(
        {"Success": "The gear was added to the character successfully"}, status=201
    )


@api_view(["POST"])
def remove_gear(request: HttpRequest):
    character_id = request.data.get("character_id")
    gear_id = request.data.get("gear_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        gear = Gear.objects.get(id=gear_id)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)

    try:
        gear_quantity = GearQuantity.objects.get(character=character, gear=gear)
        gear_quantity.delete()
    except GearQuantity.DoesNotExist:
        return Response(
            {"Error": "The gear is not associated with the character"}, status=404
        )

    return Response(
        {"Success": "The gear was removed from the character successfully"}, status=200
    )


@api_view(["POST"])
def buy_gear(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    gear_name = request.data.get("gear_name")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        gear = Gear.objects.get(name=gear_name)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)

    if character.buy_gear(gear, quantity):
        return Response({"Success": "The gear was bought successfully"}, status=200)
    else:
        return Response({"Error": "Not enough money"}, status=400)


@api_view(["POST"])
def sell_gear(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    gear_name = request.data.get("gear_name")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        gear = Gear.objects.get(name=gear_name)
    except Gear.DoesNotExist:
        return Response({"Error": "The gear does not exist"}, status=404)

    if character.sell_gear(gear, quantity):
        return Response({"Success": "The gear was sold successfully"}, status=200)
    else:
        return Response({"Error": "Not enough quantity of gear to sell"}, status=400)
