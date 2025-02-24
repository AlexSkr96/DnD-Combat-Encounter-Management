from enum import Enum

from service import AbilityType
from die import *


DamageType = Enum("Damage Type", [
    "Piercing", "Bludgeoning", "Slashing", "Fire", "Cold", "Lightning", "Radiant",
    "Necrotic", "Psychic", "Force", "Elemental", "Lightning", "Thunder", "Acid",
    "Poison", "Slashing",
])

class Damage:
    def __init__(self, damage_dice, damage_type):
        self.__damage_type = damage_type
        self.__damage_dice = damage_dice

    def deal_damage(self):
        return self.__damage_dice.roll(), self.__damage_type


class Weapon:
    def __init__(self, name, w_range = 0, reach = 0):
    # Range in feets, implies a ranged attack. None if can't make ranged attacks.
    # self.__range = w_range
    # Reach in feets, implies a meele attack. None if can't make meele attacks.
    # self.__reach = reach



class Spell:
