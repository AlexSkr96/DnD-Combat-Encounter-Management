from enum import Enum

from service import AbilityType
from die import *
from character import Character


DamageType = Enum("Damage Type", [
    "Piercing", "Bludgeoning", "Slashing", "Fire", "Cold", "Lightning", "Radiant",
    "Necrotic", "Psychic", "Force", "Elemental", "Lightning", "Thunder", "Acid",
    "Poison", "Slashing",
])

class Damage:
    def __init__(self, damage_dice: DieRoll, damage_type: DamageType):
        self.__damage_type = damage_type
        self.__damage_dice = damage_dice

    def deal_damage(self):
        return self.__damage_dice.roll(), self.__damage_type


class Attack:
    def __init__(self, ability: AbilityType):
        self.__ability = ability
        self.__damages = []

    def add_damage(self, damage: Damage):
        self.__damages.append(damage)

    # def attack(self, target: Character):



class Weapon:
    def __init__(self, name: str, w_range = 0, reach = 0):
    # Range in feets, implies a ranged attack. None if can't make ranged attacks.
    # self.__range = w_range
    # Reach in feets, implies a meele attack. None if can't make meele attacks.
    # self.__reach = reach



class Spell:
