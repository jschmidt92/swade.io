from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from discordlogin.models import DiscordUser


# Create your views here.
@api_view(["GET"])
def get_all_events(request: HttpRequest):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)


@api_view(["GET", "POST"])
def create_event(request: HttpRequest):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The event was created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_event_by_id(request: HttpRequest, id: int):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    except Event.DoesNotExist:
        return Response({"Error": "The event does not exist"}, status=404)


@api_view(["DELETE"])
def delete_event(request: HttpRequest, id: int):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return Response({"Success": "The event was deleted successfully"}, status=200)
    except Event.DoesNotExist:
        return Response({"Error": "The event does not exist"}, status=404)


@api_view(["POST"])
def get_attendance(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    event_id = request.data.get("event_id")
    try:
        event = Event.objects.get(id=event_id)
        user = DiscordUser.objects.get(id=discord_id)
        attendance = event.attendance.get(str(user.id))
        if attendance is None:
            attendance = False
        return Response({"attendance": attendance}, status=200)
    except Event.DoesNotExist:
        return Response({"Error": "The event does not exist"}, status=404)
    except DiscordUser.DoesNotExist:
        return Response({"Error": "The user does not exist"}, status=404)


@api_view(["POST"])
def update_attendance(request: HttpRequest):
    discord_id = request.data.get("discord_id")
    event_id = request.data.get("event_id")
    attendance = request.data.get("attendance")
    try:
        event = Event.objects.get(id=event_id)
        user = DiscordUser.objects.get(id=discord_id)
        event.attendance[user.id] = attendance
        event.save()
        return Response({"Success": "Attendance updated successfully"}, status=200)
    except Event.DoesNotExist:
        return Response({"Error": "The event does not exist"}, status=404)
    except DiscordUser.DoesNotExist:
        return Response({"Error": "The user does not exist"}, status=404)
