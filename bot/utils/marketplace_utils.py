from config import API_BASE_URL
import requests


def buy_cyberware(discord_id: str, character_name: str, cyberware_name: str):
    api_endpoint = f"{API_BASE_URL}/cyberware/buy/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "cyberware_name": cyberware_name,
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


def sell_cyberware(discord_id: str, character_name: str, cyberware_name: str):
    api_endpoint = f"{API_BASE_URL}/cyberware/sell/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "cyberware_name": cyberware_name,
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


def buy_gear(discord_id: str, character_name: str, gear_name: str, quantity: int):
    api_endpoint = f"{API_BASE_URL}/gear/buy/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "gear_name": gear_name,
        "quantity": quantity,
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


def sell_gear(discord_id: str, character_name: str, gear_name: str, quantity: int):
    api_endpoint = f"{API_BASE_URL}/gear/sell/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "gear_name": gear_name,
        "quantity": quantity,
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


def buy_weapon(discord_id: str, character_name: str, weapon_name: str, quantity: int):
    api_endpoint = f"{API_BASE_URL}/weapons/buy/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "weapon_name": weapon_name,
        "quantity": quantity,
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


def sell_weapon(discord_id: str, character_name: str, weapon_name: str, quantity: int):
    api_endpoint = f"{API_BASE_URL}/weapons/sell/"

    payload = {
        "discord_id": discord_id,
        "character_name": character_name,
        "weapon_name": weapon_name,
        "quantity": quantity,
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


def get_character(discord_id: str, character_name: str):
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


def get_cyberware(cyberware_name: str):
    api_endpoint = f"{API_BASE_URL}/cyberware/get/"

    payload = {"cyberware_name": cyberware_name}

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


def get_gear(gear_name: str):
    api_endpoint = f"{API_BASE_URL}/gear/get/"

    payload = {"gear_name": gear_name}

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


def get_weapon(weapon_name: str):
    api_endpoint = f"{API_BASE_URL}/weapons/get/"

    payload = {"weapon_name": weapon_name}

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


def list_cyberware():
    api_endpoint = f"{API_BASE_URL}/cyberware/"

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


def list_gear():
    api_endpoint = f"{API_BASE_URL}/gear/"

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


def list_weapons():
    api_endpoint = f"{API_BASE_URL}/weapons/"

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
