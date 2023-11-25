from collections import deque
import json
from config import MAIN_CHANNEL_ID
from dataclasses import dataclass, field
from discord.ext import commands
from typing import List, Tuple, Dict
from utils.encounter_utils import *
import asyncio
import discord
import random
import socketio


@dataclass
class Player:
    name: str
    damage: Dict[str, int]
    npc: bool = False
    cards: List[str] = field(default_factory=list)
    card_values: List[Tuple[int, int]] = field(default_factory=list)

    def deal_card(self, card: str, card_value: Tuple[int, int]) -> None:
        self.cards.append(card)
        self.card_values.append(card_value)

    def reset(self) -> None:
        self.cards.clear()
        self.card_values.clear()


class Deck:
    def __init__(self) -> None:
        self.ranks = [
            "Joker",
            "Ace",
            "King",
            "Queen",
            "Jack",
            "10",
            "9",
            "8",
            "7",
            "6",
            "5",
            "4",
            "3",
            "2",
        ]
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.card_values = {
            "Joker": (15, 5),
            "Ace": (14, 0),
            "King": (13, 0),
            "Queen": (12, 0),
            "Jack": (11, 0),
            "10": (10, 0),
            "9": (9, 0),
            "8": (8, 0),
            "7": (7, 0),
            "6": (6, 0),
            "5": (5, 0),
            "4": (4, 0),
            "3": (3, 0),
            "2": (2, 0),
        }
        self.cards = deque(self.create_deck())
        self.players = []

    def create_deck(self) -> List[str]:
        cards = ["Joker", "Joker"]
        cards.extend(
            f"{rank} of {suit}" for rank in self.ranks[1:] for suit in self.suits
        )
        random.shuffle(cards)
        return cards

    def deal_card(self, player: Player) -> None:
        if not self.cards:
            raise NoMoreCardsError("No more cards in the deck.")

        card = self.cards.popleft()
        card_value = self.get_card_value(card)
        player.deal_card(card, card_value)

    def reset(self) -> None:
        self.cards = deque(self.create_deck())
        for player in self.players:
            player.reset()

    def get_card_value(self, card: str) -> Tuple[int, int]:
        rank, _ = card.split(" of ", 1)
        rank_value, suit_value = self.card_values[rank]
        return (suit_value, rank_value)


class NoMoreCardsError(Exception):
    """Raised when there are no more cards in the deck."""

    pass


class WebSocketClient:
    def __init__(self, server_url):
        self.sio = socketio.AsyncClient(ssl_verify=False)
        self.server_url = server_url

        @self.sio.event
        async def connect():
            print("Connected to WebSocket Server")

        @self.sio.event
        async def message(data):
            print(f"Received message from server: {data}")

        asyncio.ensure_future(self.sio.connect(self.server_url))

    async def send_initiative_order(self, encounter_id, initiative_order):
        data = {"encounter_id": encounter_id, "initiative_order": initiative_order}

        print(f"Encounter ID: {encounter_id}, Initiative Order: {initiative_order}")

        await self.sio.emit("initiativeDealt", data)

    async def initiative_turn(self):
        await self.sio.emit("initiativeNextTurn")


class deck_of_cards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deck = Deck()
        self.current_turn = 0
        self.initiative_order = []
        self.websocket_client = WebSocketClient("https://135.135.196.140:3000")

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == MAIN_CHANNEL_ID
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

    @commands.command(aliases=["di", "init"])
    async def deal_initiative(
        self,
        ctx,
        encounter_id: int = commands.parameter(description="ID of encounter."),
    ):
        """
        Description: Deal the initiative order for the game. The order is based on the card value.

        Params:
        !init EncounterID

        Example:
        !init 1
        """

        char_res = get_encounter_characters(encounter_id)
        characters_data = char_res

        npc_res = get_encounter_npcs(encounter_id)
        npcs_data = npc_res

        characters = [Player(char["name"], char["damage"]) for char in characters_data]

        npcs = [Player(npc["name"], npc["damage"], npc=True) for npc in npcs_data]

        self.deck.players = characters + npcs

        for player in self.deck.players:
            try:
                self.deck.deal_card(player)
            except NoMoreCardsError as e:
                await ctx.send(str(e))
                return

        self.deck.players.sort(key=lambda player: player.card_values[-1], reverse=True)

        initiative_order = [player.name for player in self.deck.players]

        embed = self.create_initiative_embed()
        await ctx.send(embed=embed)

        current_player_embed = self.create_current_player_embed(self.deck.players[0])
        await ctx.send(embed=current_player_embed)

        await self.websocket_client.send_initiative_order(
            encounter_id, initiative_order
        )

    @commands.command(aliases=["ei", "end"])
    async def end_initiative(self, ctx):
        """
        Description: End the initiative order for the game.

        Params:
        N/A

        Example:
        !end
        """

        try:
            self.initiative_order = []
            self.current_turn = 0
            self.deck.reset()

            await self.send_embed(
                ctx,
                "Encounter Ended",
                "The Encounter has ended and the deck has been reset to a full deck.",
                discord.Color.blue(),
            )
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(aliases=["dc", "deal"])
    async def deal_card(
        self,
        ctx,
        player_name=commands.parameter(description="Player", default=None),
    ):
        """Deal a card to the specified player."""
        player = next(
            (player for player in self.deck.players if player.name == player_name), None
        )
        if player:
            try:
                self.deck.deal_card(player)
                await ctx.send(f"A card was dealt to {player.name}.")
            except NoMoreCardsError as e:
                await ctx.send(f"No more cards: {str(e)}")
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")
        else:
            await ctx.send("Player not found.")

    @commands.command(aliases=["vpc"])
    @commands.is_owner()
    async def view_player_cards(
        self,
        ctx,
        player_name=commands.parameter(description="Name of character.", default=None),
    ):
        """
        Description: View the cards of the specified character.

        Params:
        !vpc NameOfCharacter

        Example:
        !vpc John
        """

        player = next(
            (player for player in self.deck.players if player.name == player_name), None
        )
        if player:
            cards = ", ".join(player.cards)
            await ctx.author.send(f"{player.name}'s cards: {cards}")
        else:
            await ctx.send("Player not found.")

    @commands.command(aliases=["rh", "reveal"])
    async def reveal_hand(
        self,
        ctx,
        player_name=commands.parameter(description="Name of character", default=None),
    ):
        """
        Description: Reveal the hand of a specified character.

        Params:
        !rh NameOfCharacter

        Example:
        !rh John
        """

        player = next(
            (player for player in self.deck.players if player.name == player_name), None
        )
        if player:
            cards = ", ".join(player.cards)
            await ctx.send(f"{player.name} reveals their hand: {cards}")
        else:
            await ctx.send("Player not found.")

    @commands.command(aliases=["n", "nt"])
    async def next_turn(self, ctx):
        """
        Description: Go to next player in the initiative order.

        Params:
        N/A

        Example:
        !n
        """

        self.current_turn = (self.current_turn + 1) % len(self.deck.players)

        # Send the current player embed
        current_player = self.deck.players[self.current_turn]
        current_player_embed = self.create_current_player_embed(current_player)
        await ctx.send(embed=current_player_embed)

        await self.websocket_client.initiative_turn()

    def create_current_player_embed(self, player):
        damage_string = ", ".join(f"{k}: **{v}**" for k, v in player.damage.items())
        color = discord.Color.red() if player.npc else discord.Color.green()
        embed = discord.Embed(title="Current Player", color=color)
        embed.add_field(
            name=f"{player.name}'s Turn",
            value=f"Damage: {damage_string}",
            inline=False,
        )
        return embed

    async def send_embed(self, ctx, title, description, color=discord.Color.green()):
        embed = discord.Embed(title=title, color=color, description=description)
        embed.set_footer(text=f"{len(self.deck.cards)} cards remaining in the deck")
        await ctx.send(embed=embed)

    def create_initiative_embed(self):
        embed = discord.Embed(title="Initiative Order", color=discord.Color.blue())
        for i, player in enumerate(self.deck.players, start=1):
            name = f"{i}. {player.name}"
            embed.add_field(name=name, value=player.cards[-1], inline=False)
        embed.set_footer(text=f"{len(self.deck.cards)} cards remaining in the deck")
        return embed


async def setup(bot):
    await bot.add_cog(deck_of_cards(bot))
