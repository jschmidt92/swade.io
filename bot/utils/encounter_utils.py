from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_BASE_URL = str(os.environ["API_BASE_URL"])


def add_character_encounter(encounter_id: int, discord_id: str, character_name: str):
    api_endpoint = f"{API_BASE_URL}/encounters/add/character/"

    payload = {
        "encounter_id": encounter_id,
        "discord_id": discord_id,
        "character_name": character_name,
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


def add_npc_encounter(encounter_id: int, npc_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/add/npc/"

    payload = {"encounter_id": encounter_id, "npc_id": npc_id}

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


def create_encounter(name: str, notes: str, body: str):
    api_endpoint = f"{API_BASE_URL}/encounters/new/"

    payload = {"name": name, "notes": notes, "body": str}

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


def delete_encounter(encounter_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/delete/{encounter_id}/"

    try:
        response = requests.delete(api_endpoint)

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


def get_encounter_npcs(encounter_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/{encounter_id}/npcs/"

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


def remove_character_encounter(encounter_id: int, discord_id: str, character_name: str):
    api_endpoint = f"{API_BASE_URL}/encounters/remove/character/"

    payload = {
        "encounter_id": encounter_id,
        "discord_id": discord_id,
        "character_name": character_name,
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


def remove_npc_encounter(encounter_id: int, npc_id: int):
    api_endpoint = f"{API_BASE_URL}/encounters/remove/npc/"

    payload = {"encounter_id": encounter_id, "npc_id": npc_id}

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


def update_encounter(
    encounter_id: int, name: str = None, notes: str = None, body: str = None
):
    api_endpoint = f"{API_BASE_URL}/encounters/update/{encounter_id}/"
    payload = {}

    if name is not None:
        payload["name"] = name
    if notes is not None:
        payload["notes"] = notes
    if body is not None:
        payload["body"] = body

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
