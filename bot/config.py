from dotenv import load_dotenv
import discord
import json
import os

load_dotenv()

# Bot configuration
API_BASE_URL = os.getenv("API_BASE_URL")
CHARACTER_CHANNEL_ID = int(os.getenv("CHARACTER_CHANNEL_ID"))
DEFAULT_BENNY_POOL = int(os.getenv("DEFAULT_BENNY_POOL"))
MAIN_CHANNEL_ID = int(os.getenv("MAIN_CHANNEL_ID"))
MARKET_CHANNEL_ID = int(os.getenv("MARKET_CHANNEL_ID"))
OWNER_IDS_STR = os.getenv("OWNER_IDS")
OWNER_IDS = json.loads(OWNER_IDS_STR)
TOKEN = os.getenv("TOKEN")
TRACKER_CHANNEL_ID=int(os.getenv("TRACKER_CHANNEL_ID"))

# Discord intents configuration
INTENTS = discord.Intents.all()

# Prefix for bot commands
COMMAND_PREFIX = "!"

# Cogs directory
COGS_DIRECTORY = "./cogs"
