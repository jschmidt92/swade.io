from config import TRACKER_CHANNEL_ID
from discord.ext import commands
from utils.encounter_utils import *
import discord


class encounters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.encounters = {}

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == TRACKER_CHANNEL_ID
            and ctx.guild.me.guild_permissions.manage_messages
        )

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        except discord.errors.Forbidden:
            pass

    @commands.command(aliases=["ec"])
    @commands.has_role("GameMaster")
    async def encounter_create(
        self,
        ctx,
        name: str = commands.parameter(description="Name of encounter."),
        notes: str = commands.parameter(description="Notes for encounter.", default=""),
        body: str = commands.parameter(description="Body for encounter.", default=""),
    ):
        """
        Description: Create an encounter.

        Params:
        !ec NameOfEncounter

        Example:
        !ec Bandits
        """

        if not isinstance(name, str):
            await ctx.send("Encounter Name must be a string.")
            return

        # self.encounter.insert(name)
        response = create_encounter(name, notes, body)

        if response:
            await ctx.send(f"Encounter **{name}** created successfully")
        else:
            await ctx.send("An error occured")

    @commands.command(aliases=["efa"])
    @commands.has_role("GameMaster")
    async def encounter_fetch_all(self, ctx):
        """
        Description: Fetch all created encounters.

        Params:
        N/A

        Example:
        !efa
        """

        encounters = get_all_encounters()

        if encounters:
            for encounter in encounters:
                embed = discord.Embed(
                    title=f"Encounter: {encounter['name']}",
                    description=encounter["notes"]
                    if encounter["notes"] != "N/A"
                    else "None",
                )

                characters = encounter["characters"]
                if characters:
                    characters_value = ""
                    for character in characters:
                        characters_value += f"{character['name']} - Inc: {character['damage']['Inc']}, Wounds: {character['damage']['Wounds']}, Fatigue: {character['damage']['Fatigue']}\n"
                    embed.add_field(
                        name="Characters", value=characters_value, inline=False
                    )
                else:
                    embed.add_field(name="Characters", value="None", inline=False)

                npcs = encounter["npcs"]
                if npcs:
                    npcs_value = ""
                    for npc in npcs:
                        npcs_value += f"{npc['name']} - Inc: {npc['damage']['Inc']}, Wounds: {npc['damage']['Wounds']}, Fatigue: {npc['damage']['Fatigue']}\n"
                    embed.add_field(name="NPCs", value=npcs_value, inline=False)
                else:
                    embed.add_field(name="NPCs", value="None", inline=False)

                await ctx.send(embed=embed)
        else:
            await ctx.send("An error occurred.")

    @commands.command(aliases=["ed"])
    @commands.has_role("GameMaster")
    async def encounter_delete(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
    ):
        """
        Description: Delete an encounter.

        Params:
        !ed EncounterID

        Example:
        !ed 1
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an integer.")
            return

        response = delete_encounter(encounter_id)

        if response:
            await ctx.send(f"Encounter **{encounter_id}** deleted successfully")
        else:
            await ctx.send("An error occured")

    @commands.command(aliases=["eac"])
    @commands.has_role("GameMaster")
    async def encounter_add_character(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
        player: discord.User = commands.parameter(
            description="User ID of whome to fetch character."
        ),
        name: str = commands.parameter(description="Name of character."),
    ):
        """
        Description: Add character to encounter.

        Params:
        !eac EncounterID UserID NameOfCharacter

        Example:
        !eac 1 1234567890 John
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an integer.")
            return

        if not isinstance(player, object):
            await ctx.send("Player must be an object.")
            return

        if not isinstance(name, str):
            await ctx.send("Name must be a string.")
            return

        response = add_character_encounter(encounter_id, player.id, name)

        if response:
            embed = discord.Embed(
                title="Character Added to Encounter",
                description=f"Character **{name}** added to encounter successfully",
                color=discord.Color.yellow(),
            )

            await ctx.send(embed=embed)
        else:
            await ctx.send("An error occured")

    @commands.command(aliases=["efc"])
    @commands.has_role("GameMaster")
    async def encounter_fetch_characters(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
    ):
        """
        Description: Fetch all characters in encounter.

        Params:
        !efc EncounterID

        Example:
        !efc 1
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an int.")
            return

        encounter_data = get_encounter(encounter_id)

        if not encounter_data:
            await ctx.send("Encounter not found.")
            return

        encounter_name = encounter_data["name"]
        characters = encounter_data["characters"]

        embed = discord.Embed(
            title="Characters in Encounter",
            description=f"Encounter **{encounter_name}**",
            color=0x00FF00,
        )

        for character in characters:
            name = character["name"]
            inc = character["damage"]["Inc"]
            wounds = character["damage"]["Wounds"]
            fatigue = character["damage"]["Fatigue"]
            health = f"Inc: {inc}, Wounds: {wounds}, Fatigue: {fatigue}"
            embed.add_field(name="Character Name:", value=name, inline=False)
            embed.add_field(name="Health:", value=health, inline=True)

        await ctx.send(embed=embed)

    @commands.command(aliases=["erc"])
    @commands.has_role("GameMaster")
    async def encounter_remove_character(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
        player: discord.User = commands.parameter(
            description="User ID to whome to fetch character."
        ),
        name: str = commands.parameter(description="Name of character."),
    ):
        """
        Description: Remove a character from encounter.

        Params:
        !erc EncounterID UserID NameOfCharacter

        Example:
        !erc 1 1234567890 John
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an integer.")
            return

        if not isinstance(player, object):
            await ctx.send("Player must be an object.")
            return

        if not isinstance(name, str):
            await ctx.send("Name must be a string.")
            return

        response = remove_character_encounter(encounter_id, player.id, name)

        if response:
            embed = discord.Embed(
                title="Character Removed from Encounter",
                description=f"Character **{name}** removed from encounter successfully",
                color=discord.Color.yellow(),
            )

            await ctx.send(embed=embed)
        else:
            await ctx.send("An error occured")

    @commands.command(aliases=["ean"])
    @commands.has_role("GameMaster")
    async def encounter_add_npc(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
        npc_id: int = commands.parameter(description="ID of npc."),
    ):
        """
        Description: Add a npc to encounter.

        Params:
        !ean EncounterID NPCID

        Example:
        !ean 1 1
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an integer.")
            return

        if not isinstance(npc_id, int):
            await ctx.send("NPC ID must be an integer.")
            return

        response = add_npc_encounter(encounter_id, npc_id)

        if response:
            embed = discord.Embed(
                title="NPC Added to Encounter",
                description=f"NPC added to encounter successfully",
                color=discord.Color.yellow(),
            )

            await ctx.send(embed=embed)
        else:
            await ctx.send("An error occured")

    @commands.command(aliases=["efn"])
    @commands.has_role("GameMaster")
    async def encounter_fetch_npcs(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
    ):
        """
        Description: Fetch all npcs in encounter.

        Params:
        !efn EncounterID

        Example:
        !efn 1
        """
        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an int.")
            return

        encounter_data = get_encounter(encounter_id)

        if not encounter_data:
            await ctx.send("Encounter not found.")
            return

        encounter_name = encounter_data["name"]
        npcs = encounter_data["npcs"]

        embed = discord.Embed(
            title="NPCs in Encounter",
            description=f"Encounter **{encounter_name}**",
            color=0xFF0000,
        )

        for npc in npcs:
            npc_name = npc["name"]
            inc = npc["damage"]["Inc"]
            wounds = npc["damage"]["Wounds"]
            fatigue = npc["damage"]["Fatigue"]
            health = f"Inc: {inc}, Wounds: {wounds}, Fatigue: {fatigue}"
            embed.add_field(name="NPC Name:", value=npc_name, inline=False)
            embed.add_field(name="Health:", value=health, inline=True)

        await ctx.send(embed=embed)

    @commands.command(aliases=["ern"])
    @commands.has_role("GameMaster")
    async def encounter_remove_npc(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
        npc_id: int = commands.parameter(description="ID of npc."),
    ):
        """
        Description: Remove a npc from encounter.

        Params:
        !ern EncounterID NPCID

        Example:
        !ern 1 1
        """

        if not isinstance(encounter_id, int):
            await ctx.send("Encounter ID must be an integer.")
            return

        if not isinstance(npc_id, int):
            await ctx.send("NPC ID must be an integer.")
            return

        response = remove_npc_encounter(encounter_id, npc_id)

        if response:
            embed = discord.Embed(
                title="NPC Removed from Encounter",
                description=f"NPC removed from encounter successfully",
                color=discord.Color.yellow(),
            )

            await ctx.send(embed=embed)
        else:
            await ctx.send("An error occured")


async def setup(bot):
    await bot.add_cog(encounters(bot))
