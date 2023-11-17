from config import MARKET_CHANNEL_ID
from discord.ext import commands
from utils.marketplace_utils import *
import discord


class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == MARKET_CHANNEL_ID
            and ctx.guild.me.guild_permissions.manage_messages
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "Missing argument. Please check the command syntax and try again."
            )

    async def list_items(self, ctx, list_func, item_type):
        items = list_func()

        if not items:
            await ctx.send("The store is currently empty.")
            return

        message = f"{item_type.capitalize()} available in the store:\n"
        for item in items:
            message += f"{item['name']}: **${item['price']}**"
            if item_type == "weapons":
                message += f"Min-Strength: **{item['min_str']}**\n"
            else:
                message += f"\n"

        await ctx.send(message)

    @commands.command()
    async def view_cyberware(self, ctx):
        """
        Description: View cyberware in store.

        Params:
        N/A

        Example:
        !view_cyberware
        """

        await self.list_items(ctx, list_cyberware, "cyberware")

    @commands.command()
    async def view_gear(self, ctx):
        """
        Description: View gear in store.

        Params:
        N/A

        Example:
        !view_gear
        """

        await self.list_items(ctx, list_gear, "gear")

    @commands.command()
    async def view_weapons(self, ctx):
        """
        Description: View weapons in store.

        Params:
        N/A

        Example:
        !view_weapons
        """

        await self.list_items(ctx, list_weapons, "weapons")

    async def buy_item(
        self,
        ctx,
        character_name,
        item_name,
        player,
        buy_func,
        get_func,
        item_type,
        quantity=1,
    ):
        discord_id = player.id if player else str(ctx.author.id)

        character_response = get_character(discord_id, character_name)
        if not character_response:
            await ctx.send("Failed to retrieve character.")
            return

        character = character_response
        character_money = character.get("money", 0)

        item_response = get_func(item_name)
        if not item_response:
            await ctx.send(f"Failed to retrieve {item_type}.")
            return

        item = item_response
        item_price = item.get("price", 0)
        total_price = item_price * quantity

        if character_money < total_price:
            await ctx.send("You don't have enough money.")
            return

        response = buy_func(discord_id, character_name, item_name, quantity)

        if response:
            await ctx.send(
                f"Your character **{character_name}** has bought {quantity} unit(s) of {item_name}."
            )
        else:
            await ctx.send("An error occurred.")

    @commands.command()
    async def buy_cyberware(
        self,
        ctx,
        character_name: str = commands.parameter(description="Name of character."),
        cyberware_name: str = commands.parameter(description="Name of cyberware."),
        player: discord.User = commands.parameter(
            description="User ID to fetch character", default=None
        ),
    ):
        """
        Description: Buy an cyberware from store.

        Params:
        !buy_cyberware NameOfCharacter NameOfCyberware

        Example:
        !buy_cyberware John "Adrenal Surge (1)"
        !buy_cyberware John "Adrenal Surge (1)" 1234567890
        """

        await self.buy_item(
            ctx,
            character_name,
            cyberware_name,
            player,
            buy_cyberware,
            get_cyberware,
            "cyberware",
        )

    @commands.command()
    async def buy_gear(
        self,
        ctx,
        character_name: str = commands.parameter(description="Name of character."),
        gear_name: str = commands.parameter(description="Name of gear."),
        quantity: int = commands.parameter(description="Quantity to buy", default=1),
        player: discord.User = commands.parameter(
            description="User ID to fetch character", default=None
        ),
    ):
        """
        Description: Buy an gear from store.

        Params:
        !buy_gear NameOfCharacter NameOfGear Quantity

        Example:
        !buy_gear John Tent 1
        !buy_gear John Tent 1 1234567890
        """

        await self.buy_item(
            ctx,
            character_name,
            gear_name,
            player,
            buy_gear,
            get_gear,
            "gear",
            quantity,
        )

    @commands.command()
    async def buy_weapon(
        self,
        ctx,
        character_name: str = commands.parameter(description="Name of character."),
        weapon_name: str = commands.parameter(description="Name of weapon."),
        quantity: int = commands.parameter(description="Quantity to buy", default=1),
        player: discord.User = commands.parameter(
            description="User ID to fetch character", default=None
        ),
    ):
        """
        Description: Buy an weapon from store.

        Params:
        !buy_weapon NameOfCharacter NameOfWeapon Quantity

        Example:
        !buy_weapon John Machete 1
        !buy_weapon John Machete 1 1234567890
        """

        await self.buy_item(
            ctx,
            character_name,
            weapon_name,
            player,
            buy_weapon,
            get_weapon,
            "weapon",
            quantity,
        )

    @commands.command()
    async def view_money(
        self,
        ctx,
        character_name: str = commands.parameter(description="Name of character"),
        player: discord.User = commands.parameter(
            description="User ID to fetch character", default=None
        ),
    ):
        """
        Description: View character's money.

        Params:
        !view_money NameOfCharacter UserID

        Example:
        !view_money John
        """

        discord_id = player.id if player else str(ctx.author.id)

        character_response = get_character(discord_id, character_name)
        if not character_response.ok:
            await ctx.send("Failed to retrieve character.")
            return

        character = character_response
        character_money = character.get("money", 0)

        if character_money:
            await ctx.author.send(
                f"Character **{character_name}** has ${character_money}."
            )
        else:
            await ctx.send("An error occurred.")


async def setup(bot):
    await bot.add_cog(marketplace(bot))
