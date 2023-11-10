from config import CHARACTER_CHANNEL_ID
from discord.ext import commands
from dotenv import load_dotenv
from utils.character_utils import *
import discord
import requests

load_dotenv()


class Characters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.character_channel_id = int(os.getenv("CHARACTER_CHANNEL_ID"))

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == self.character_channel_id
            and ctx.guild.me.guild_permissions_manage_messages
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "Missing Argument. Please check the command syntax and try again."
            )

    def create_character_embed(self, character):
        cyberware = [
            f"{item['name']} (Strain: {item['strain']}, Effect: {item['effect']}, Notes: ({item['notes']})"
            for item in character["cyberware"]
        ]

        powers = [
            f"{power['name']} PP: ({power['pp']}, Range: {power['range']}, Duration: {power['duration']}), Effect: {power['effect']}, Notes: ({power['notes']})"
            for power in character["powers"]
        ]

        gear = [
            f"({item['quantity']}x) {item['gear']['name']} (Min Str: {item['gear'][['min_str']]}, Weight: {item['gear']['wt']}, Notes: {item['gear']['notes']})"
            for item in character["gear"]
        ]

        weapons = [
            f"({weapon['quantity']}x) {weapon['weapon']['name']} (Range: {weapon['weapon']['range']}, Damage: {weapon['weapon']['damage']}, ROF: {weapon['weapon']['rof']}, Shots: {weapon['weapon']['shots']}, Min Str: {weapon['weapon']['min_str']}, Weight: {weapon['weapon']['wt']})"
            for weapon in character["weapons"]
        ]

        hindrances = character["hindrances"] or "None"
        edges = character["edges"] or "None"

        attributes = "\n".join(
            f"{k}: **{v}**" for k, v in character["attributes"].items()
        )
        skills = "\n".join(f"{k}: **{v}**" for k, v in character["skills"].items())

        embed = discord.Embed(
            title=f"Character **{character['name']}**",
            description=f"Race: **{character['race']}** \n Gender: **{character['gender']}** \n Charisma: **{character['charisma']}** \n Pace: **{character['pace']}** \n Parry: **{character['parry']}** \n Toughness: **{character['toughness']}**",
            color=discord.Color.green(),
        )
        embed.add_field(name="Attributes", value=attributes, inline=False)
        embed.add_field(name="Skills", value=skills, inline=False)
        embed.add_field(
            name="Cyberware",
            value="\n".join(cyberware) if cyberware else "None",
            inline=False,
        )
        embed.add_field(
            name="Gear", value="\n".join(gear) if gear else "None", inline=False
        )
        embed.add_field(name="Hindrances", value=hindrances, inline=False)
        embed.add_field(name="Edges", value=edges, inline=False)
        embed.add_field(
            name="Powers", value="\n".join(powers) if powers else "None", inline=False
        )
        embed.add_field(
            name="Weapons",
            value="\n".join(weapons) if weapons else "None",
            inline=False,
        )
        embed.add_field(name="Money", value=str(character["money"]), inline=False)

        return embed

    async def send_character(self, ctx, player, character_name, send_to_author=False):
        discord_id = player.id if player else str(ctx.author.id)

        try:
            response = get_player_character(discord_id, character_name)
            response.raise_for_status()
            character = response.json()
        except requests.exceptions.RequestException as e:
            await ctx.author.send(f"Error getting characters: {e}")
            return

        if not character:
            await ctx.author.send("Player doesn't have any characters yet.")
            return

        embed = self.create_character_embed(character)

        if send_to_author:
            await ctx.author.send(embed=embed)
        else:
            await ctx.send(embed=embed)

    @commands.command(aliases=["display"])
    async def display_character(
        self,
        ctx,
        character_name: str,
        player: discord.User = None,
    ):
        """
        Description: Display a character.

        Params:
        !display NameOfCharacter UserID

        Example:
        !display John
        !display John 1234567890
        """

        await self.send_character(ctx, player, character_name)

    @commands.command(aliases=["view"])
    async def view_character(
        self,
        ctx,
        character_name: str,
        player: discord.User = None,
    ):
        """
        Description: Display a character.

        Params:
        !view NameOfCharacter UserID

        Example:
        !view John
        !view John 1234567890
        """

        await self.send_character(ctx, player, character_name, send_to_author=True)

    @commands.command(aliases=["list"])
    async def list_characters(
        self,
        ctx,
        player: discord.User = None,
    ):
        """
        Description: View list of player characters.

        Params:
        !list UserID

        Example:
        !list 1234567890
        """

        discord_id = player.id if player else str(ctx.author.id)

        try:
            response = get_player_characters(discord_id)
            response.raise_for_status()
            characters = response.json()
        except requests.exceptions.RequestException as e:
            await ctx.author.send(f"Error getting characters: {e}")
            return

        if not characters:
            await ctx.author.send("Player doesn't have any characters yet.")
            return

        for character in characters:
            embed = self.create_character_embed(character)
            await ctx.author.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Characters(bot))
