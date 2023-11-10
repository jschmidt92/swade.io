from dotenv import load_dotenv
import discord
import json
import os

load_dotenv()

# Bot configuration
API_BASE_URL = os.getenv("API_BASE_URL")
CHARACTER_CHANNEL_ID = os.getenv("CHARACTER_CHANNEL_ID")
MAIN_CHANNEL_ID = int(os.getenv("MAIN_CHANNEL_ID"))
OWNER_IDS_STR = os.getenv("OWNER_IDS")
OWNER_IDS = json.loads(OWNER_IDS_STR)
TOKEN = os.getenv("TOKEN")

# Discord intents configuration
INTENTS = discord.Intents.all()

# Prefix for bot commands
COMMAND_PREFIX = "!"

# Cogs directory
COGS_DIRECTORY = "./cogs"
