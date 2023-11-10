from django.db import models
from cyberware.models import Cyberware
from gear.models import Gear
from power.models import Power
from weapon.models import Weapon
from marketplace.models import Transaction

# Create your models here.
CHAR_GENDER = [("male", "Male"), ("female", "Female")]

CHAR_RACE = [
    ("android", "Android"),
    ("aquarian", "Aquarian"),
    ("aurax", "Aurax"),
    ("avion", "Avion"),
    ("construct", "Construct"),
    ("deader", "Deader"),
    ("dwarf", "Dwarf"),
    ("elf", "Elf"),
    ("floran", "Floran"),
    ("halfelve", "Half-Elve"),
    ("halffolk", "Half-Folk"),
    ("human", "Human"),
    ("insectoid", "Insectoid"),
    ("kalian", "Kalian"),
    ("rakashan", "Rakashan"),
    ("robot", "Robot"),
    ("saurian", "Saurian"),
    ("serran", "Serran"),
    ("yeti", "Yeti"),
]

def default_damage():
    return {"Wounds": 0, "Fatigue": 0, "Inc": "No"}

class Character(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255, choices=CHAR_RACE)
    gender = models.CharField(max_length=255, choices=CHAR_GENDER)
    discordID = models.CharField(max_length=255)
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
    # player = models.ForeignKey(DiscordUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def buy_cyberware(self, cyberware, quantity=1):
        total_price = cyberware.price * quantity
        if self.money >= total_price:
            self.money -= total_price
            self.cyberware.add(cyberware)
            self.save()
            transaction = Transaction(character=self, amount=cyberware.price * quantity, transaction_type='buy', item_type='cyberware', item_id=cyberware.id)
            transaction.save()
            return True
        else:
            return False

    def sell_cyberware(self, cyberware, quantity=1):
        if self.cyberware.filter(id=cyberware.id).exists():
            self.money += cyberware.price * quantity
            self.cyberware.remove(cyberware)
            self.save()
            transaction = Transaction(character=self, amount=cyberware.price * quantity, transaction_type='sell', item_type='cyberware', item_id=cyberware.id)
            transaction.save()
            return True
        else:
            return False

    def buy_gear(self, gear, quantity=1):
        gear_cost = gear.price * quantity
        if self.money >= gear_cost:
            self.money -= gear_cost
            self.gear.add(gear)
            gear_quantity, created = GearQuantity.objects.get_or_create(
                character=self, gear=gear
            )
            gear_quantity.quantity += quantity
            gear_quantity.save()
            self.save()
            transaction = Transaction(character=self, amount=gear.price * quantity, transaction_type='buy', item_type='gear', item_id=gear.id)
            transaction.save()
            return True
        else:
            return False

    def sell_gear(self, gear, quantity=1):
        gear_quantity = GearQuantity.objects.filter(character=self, gear=gear).first()
        if gear_quantity and gear_quantity.quantity >= quantity:
            self.money += gear.price * quantity
            gear_quantity.quantity -= quantity
            if gear_quantity.quantity == 0:
                gear_quantity.delete()
            else:
                gear_quantity.save()
            self.save()
            transaction = Transaction(character=self, amount=gear.price * quantity, transaction_type='sell', item_type='gear', item_id=gear.id)
            transaction.save()
            return True
        else:
            return False

    def buy_weapon(self, weapon, quantity=1):
        weapon_cost = weapon.price * quantity
        if self.money >= weapon_cost:
            self.money -= weapon_cost
            self.weapons.add(weapon)
            weapon_quantity, created = WeaponQuantity.objects.get_or_create(
                character=self, weapon=weapon
            )
            weapon_quantity.quantity += quantity
            weapon_quantity.save()
            self.save()
            transaction = Transaction(character=self, amount=weapon.price * quantity, transaction_type='buy', item_type='weapon', item_id=weapon.id)
            transaction.save()
            return True
        else:
            return False

    def sell_weapon(self, weapon, quantity=1):
        weapon_quantity = WeaponQuantity.objects.filter(
            character=self, weapon=weapon
        ).first()
        if weapon_quantity and weapon_quantity.quantity >= quantity:
            self.money += weapon.price * quantity
            weapon_quantity.quantity -= quantity
            if weapon_quantity.quantity == 0:
                weapon_quantity.delete()
            else:
                weapon_quantity.save()
            self.save()
            transaction = Transaction(character=self, amount=weapon.price * quantity, transaction_type='buy', item_type='weapon', item_id=weapon.id)
            transaction.save()
            return True
        else:
            return False

class GearQuantity(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    gear = models.ForeignKey(
        Gear, on_delete=models.CASCADE, related_name="character_gear"
    )
    quantity = models.PositiveIntegerField(default=0)


class WeaponQuantity(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        Weapon, on_delete=models.CASCADE, related_name="character_weapon"
    )
    quantity = models.PositiveIntegerField(default=0)
