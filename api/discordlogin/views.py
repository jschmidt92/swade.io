from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from .models import DiscordUser
import os
import requests

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUTH_URL_DISCORD = os.getenv("AUTH_URL_DISCORD")


# Create your views here.
@login_required(login_url="/discord/oauth2/login")
def get_authenticated_user(request: HttpRequest):
    user = request.user
    return JsonResponse(
        {
            "id": str(user.id),
            "username": user.username,
            "global_name": user.global_name,
            "avatar": user.avatar,
            "mfa_enabled": user.mfa_enabled,
            "locale": user.locale,
            "email": user.email,
            "verified": user.verified,
            "last_login": user.last_login,
            "is_gm": user.is_gm,
            "is_player": user.is_player,
            "date_joined": user.date_joined
        }
    )

def get_user_by_id(request: HttpRequest, discord_id: str):
    try:
        user = DiscordUser.objects.get(id=discord_id)
    except DiscordUser.DoesNotExist:
        raise Http404("User not found")
    
    return JsonResponse({
        "id": str(user.id),
        "username": user.username,
        "global_name": user.global_name,
        "avatar": user.avatar,
        "mfa_enabled": user.mfa_enabled,
        "locale": user.locale,
        "email": user.email,
        "verified": user.verified,
        "last_login": user.last_login,
        "is_gm": user.is_gm,
        "is_player": user.is_player,
        "date_joined": user.date_joined
    })


def discord_login(request: HttpRequest):
    return redirect(AUTH_URL_DISCORD)


def discord_login_redirect(request: HttpRequest):
    code = request.GET.get("code")
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    access_token = user.get("access_token", None)
    if discord_user:
        login(request, discord_user)
        return redirect(f"http://localhost:5173?token={access_token}&discord_id={user['id']}")
    else:
        return redirect("/discord/oauth2/login")


def exchange_code(code: str):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "scope": "identify email",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers
    )
    credentials = response.json()
    access_token = credentials["access_token"]
    response = requests.get(
        "%s/users/@me" % API_ENDPOINT,
        headers={"Authorization": "Bearer %s" % access_token},
    )
    user = response.json()
    user["access_token"] = access_token
    return user
