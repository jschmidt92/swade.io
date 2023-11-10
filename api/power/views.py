from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Power
from .serializers import PowerSerializer
from character.models import *

# Create your views here.
@api_view(["GET"])
def get_all_powers(request: HttpRequest):
    powers = Power.objects.all()
    serializer = PowerSerializer(powers, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_power(request: HttpRequest):
    data = request.data
    serializer = PowerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The power was created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_power(request: HttpRequest, power_id: int):
    try:
        power = Power.objects.get(id=power_id)
        serializer = PowerSerializer(power)
        return Response(serializer.data)
    except Power.DoesNotExist:
        return Response({"Error": "The power does not exist"}, status=404)


@api_view(["DELETE"])
def delete_power(request: HttpRequest, power_id: int):
    try:
        power = Power.objects.get(id=power_id)
        power.delete()
        return Response({"Success": "The power was deleted successfully"}, status=200)
    except Power.DoesNotExist:
        return Response({"Error": "The power does not exist"}, status=404)


@api_view(["POST"])
def add_power(request: HttpRequest):
    character_id = request.data.get("character_id")
    power_id = request.data.get("power_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        power = Power.objects.get(id=power_id)
    except Power.DoesNotExist:
        return Response({"Error": "The power does not exist"}, status=404)

    character.powers.add(power)

    return Response(
        {"Success": "The power was added to the character successfully"}, status=201
    )


@api_view(["POST"])
def remove_power(request: HttpRequest):
    character_id = request.data.get("character_id")
    power_id = request.data.get("power_id")

    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        return Response({"Error": "The character does not exist"}, status=404)

    try:
        power = Power.objects.get(id=power_id)
    except Power.DoesNotExist:
        return Response({"Error": "The power does not exist"}, status=404)

    character.powers.remove(power)

    return Response(
        {"Success": "The power was removed from the character successfully"},
        status=200,
    )
