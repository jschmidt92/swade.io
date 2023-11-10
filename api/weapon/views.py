from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Weapon
from .serializers import WeaponSerializer
from character.models import *

# Create your views here.
@api_view(["GET"])
def get_all_weapons(request: HttpRequest):
    weapons = Weapon.objects.all()
    serializer = WeaponSerializer(weapons, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_weapon(request: HttpRequest):
    data = request.data
    serializer = WeaponSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The weapon was created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_weapon(request: HttpRequest, weapon_id: int):
    try:
        weapon = Weapon.objects.get(id=weapon_id)
        serializer = WeaponSerializer(weapon)
        return Response(serializer.data)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)


@api_view(["GET"])
def get_weapon_by_name(request: HttpRequest):
    weapon_name = request.data.get("weapon_name")
    try:
        weapon = Weapon.objects.get(name=weapon_name)
        serializer = WeaponSerializer(weapon)
        return Response(serializer.data)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)


@api_view(["DELETE"])
def delete_weapon(request: HttpRequest, weapon_id: int):
    try:
        weapon = Weapon.objects.get(id=weapon_id)
        weapon.delete()
        return Response({"Success": "The weapon was deleted successfully"}, status=200)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)


@api_view(["POST"])
def add_weapon(request: HttpRequest):
    character_id = request.data.get("character_id")
    weapon_id = request.data.get("weapon_id")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        weapon = Weapon.objects.get(id=weapon_id)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)

    weapon_quantity, created = WeaponQuantity.objects.get_or_create(
        character=character, weapon=weapon, defaults={"quantity": quantity}
    )
    if not created:
        weapon_quantity.quantity += quantity
        weapon_quantity.save()

    return Response(
        {"Success": "The weapon was added to the character successfully"}, status=201
    )


@api_view(["POST"])
def remove_weapon(request: HttpRequest):
    character_id = request.data.get("character_id")
    weapon_id = request.data.get("weapon_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        weapon = Weapon.objects.get(id=weapon_id)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)

    try:
        weapon_quantity = WeaponQuantity.objects.get(character=character, weapon=weapon)
        weapon_quantity.delete()
    except WeaponQuantity.DoesNotExist:
        return Response(
            {"Error": "The weapon is not associated with the character"}, status=404
        )

    return Response(
        {"Success": "The weapon was removed from the character successfully"},
        status=200,
    )


@api_view(["POST"])
def buy_weapon(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    weapon_name = request.data.get("weapon_name")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        weapon = Weapon.objects.get(name=weapon_name)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)

    if character.buy_weapon(weapon, quantity):
        return Response({"Success": "The weapon was bought successfully"}, status=200)
    else:
        return Response({"Error": "Not enough money"}, status=400)


@api_view(["POST"])
def sell_weapon(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    character_name = request.data.get("character_name")
    weapon_name = request.data.get("weapon_name")
    quantity = request.data.get("quantity", 1)

    try:
        character = Character.objects.get(name=character_name, discordID=discord_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        weapon = Weapon.objects.get(name=weapon_name)
    except Weapon.DoesNotExist:
        return Response({"Error": "The weapon does not exist"}, status=404)

    if character.sell_weapon(weapon, quantity):
        return Response({"Success": "The weapon was sold successfully"}, status=200)
    else:
        return Response({"Error": "Not enough quantity of weapon to sell"}, status=400)
