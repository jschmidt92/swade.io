from config import API_BASE_URL
import requests


def get_all_characters():
    api_endpoint = f"{API_BASE_URL}/characters/"

    try:
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_player_character(discord_id, character_name):
    api_endpoint = f"{API_BASE_URL}/characters/get/"

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


def get_player_characters(discord_id):
    api_endpoint = f"{API_BASE_URL}/characters/list/{discord_id}"

    try:
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
