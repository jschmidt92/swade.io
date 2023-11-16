from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_BASE_URL = str(os.environ["API_BASE_URL"])



def add_character_encounter(encounter_id: int, player_id: str, name: str):
    api_endpoint = f"{API_BASE_URL}/encounters/add/character/"

    payload = {"encounter_id": encounter_id, "player_id": player_id, "name": name}

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


def add_monster_encounter(encounter_id: int, monster_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/add/monster/"

    payload = {"encounter_id": encounter_id, "monster_id": monster_id}

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


def get_all_encounters():
    api_endpoint = f"{API_BASE_URL}/encounters/"

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


def get_encounter(encounter_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/{encounter_id}/"

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


def get_encounter_characters(encounter_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/{encounter_id}/characters/"

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


def get_encounter_monsters(encounter_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/{encounter_id}/monsters/"

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
