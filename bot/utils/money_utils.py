from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_BASE_URL = str(os.environ["API_BASE_URL"])


def add_money(discord_id: str, character_name: str, amount: int):
    api_endpoint = f"{API_BASE_URL}/characters/add/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "amount": amount,
    }

    try:
        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def subtract_money(discord_id: str, character_name: str, amount: int):
    api_endpoint = f"{API_BASE_URL}/characters/remove/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "amount": amount,
    }

    try:
        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def check_money(discord_id: str, character_name: str):
    api_endpoint = f"{API_BASE_URL}/characters/money/"

    payload = {"discord_id": discord_id, "character_name": character_name}

    try:
        response = requests.get(api_endpoint, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
