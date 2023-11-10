from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NPC
from .serializers import NPCSerializer

# Create your views here.
@api_view(["GET"])
def get_all_npcs(request: HttpRequest):
    npcs = NPC.objects.all()
    serializer = NPCSerializer(npcs, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_npc(request: HttpRequest):
    data = request.data
    serializer = NPCSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The npc was created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_npc(request: HttpRequest, npc_id: int):
    try:
        npc = NPC.objects.get(id=npc_id)
        serializer = NPCSerializer(npc)
        return Response(serializer.data)
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)


@api_view(["DELETE"])
def delete_npc(request: HttpRequest, npc_id: int):
    try:
        npc = NPC.objects.get(id=npc_id)
        npc.delete()
        return Response({"Success": "The npc was deleted successfully"}, status=200)
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)


@api_view(["GET"])
def get_money(request: HttpRequest, npc_id: int):
    try:
        npc = NPC.objects.get(id=npc_id)
        return Response({"money": npc.money})
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)


@api_view(["POST"])
def add_money(request: HttpRequest):
    npc_id = request.data.get("npc_id")
    amount = request.data.get("amount")
    try:
        npc = NPC.objects.get(id=npc_id)
        npc.money += int(amount)
        npc.save()
        return Response(
            {
                "Success": f"Added ${amount} to {npc.name}",
                "Total Money": npc.money,
            }
        )
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)


@api_view(["POST"])
def remove_money(request: HttpRequest):
    npc_id = request.data.get("npc_id")
    amount = request.data.get("amount")
    try:
        npc = NPC.objects.get(id=npc_id)
        if npc.money >= int(amount):
            npc.money -= int(amount)
            npc.save()
            return Response(
                {
                    "Success": f"Removed {amount} from {npc.name}",
                    "Total Money": npc.money,
                }
            )
        else:
            return Response({"Error": "Not enough money"}, status=400)
    except NPC.DoesNotExist:
        return Response({"Error": "The npc does not exist"}, status=404)
