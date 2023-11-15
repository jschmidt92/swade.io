from django.db import models
from cyberware.models import Cyberware
from gear.models import Gear
from power.models import Power
from weapon.models import Weapon

# Create your models here.
CHAR_GENDER = [("male", "Male"), ("female", "Female")]


CHAR_FACTION = [("unknown", "Unknown"), ("neutral", "Neutral"), ("friendly", "Friendly"), ("enemy", "Enemy")]


CHAR_RACE = [
    ("android", "Android"),
    ("angler", "Angler"),
    ("anklebiter", "Anklebiter"),
    ("apex", "A-Pex"),
    ("aquarian", "Aquarian"),
    ("aurax", "Aurax"),
    ("avion", "Avion"),
    ("behemoth", "Behemoth"),
    ("bloodwing", "Bloodwig"),
    ("boomer", "Boomer"),
    ("colemata", "Colemata"),
    ("construct", "Construct"),
    ("deader", "Deader"),
    ("deathcrawler", "Death Crawler (Swarm)"),
    ("drake", "Drake"),
    ("dwarf", "Dwarf"),
    ("elf", "Elf"),
    ("floran", "Floran"),
    ("grazer", "Grazer"),
    ("halfelve", "Half-Elve"),
    ("halffolk", "Half-Folk"),
    ("human", "Human"),
    ("hunter", "Hunter"),
    ("insectoid", "Insectoid"),
    ("kalian", "Kalian"),
    ("krok", "Krok"),
    ("krokgiant", "Krok, Giant"),
    ("lightningdarter", "Lightning Darter (Swarm)"),
    ("lacerauns", "Lacerauns"),
    ("mauler", "Mauler"),
    ("rakashan", "Rakashan"),
    ("ravager", "Ravager"),
    ("robot", "Robot"),
    ("sailfin", "Sailfin"),
    ("saurian", "Saurian"),
    ("scrat", "Scrat"),
    ("scuteboar", "Scute Boar"),
    ("serran", "Serran"),
    ("scylla", "Scylla"),
    ("scyllagiant", "Scylla, Giant"),
    ("sirencreeper", "Siren Creeper"),
    ("spitter", "Spitter"),
    ("yeti", "Yeti"),
]


def default_damage():
    return {"Wounds": 0, "Fatigue": 0, "Inc": "No"}


class NPC(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255, choices=CHAR_RACE)
    gender = models.CharField(max_length=255, choices=CHAR_GENDER)
    faction = models.CharField(max_length=255, choices=CHAR_FACTION, default="unknown")
    charisma = models.IntegerField(default=0)
    pace = models.IntegerField(default=0)
    parry = models.IntegerField(default=0)
    toughness = models.IntegerField(default=0)
    attributes = models.JSONField()
    skills = models.JSONField()
    gear = models.ManyToManyField(Gear, through="GearQuantity", blank=True)
    hindrances = models.TextField(blank=True)
    edges = models.TextField(blank=True)
    powers = models.ManyToManyField(Power, blank=True)
    cyberware = models.ManyToManyField(Cyberware, blank=True)
    weapons = models.ManyToManyField(Weapon, through="WeaponQuantity", blank=True)
    damage = models.JSONField(default=default_damage)
    ammo = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class GearQuantity(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    gear = models.ForeignKey(
        Gear, on_delete=models.CASCADE, related_name="npc_gear"
    )
    quantity = models.PositiveIntegerField(default=0)


class WeaponQuantity(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        Weapon, on_delete=models.CASCADE, related_name="npc_weapon"
    )
    quantity = models.PositiveIntegerField(default=0)
