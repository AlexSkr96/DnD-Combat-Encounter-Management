from enum import Enum

from service import AbilityType


DamageType = Enum("Damage Type", [
    "Piercing", "Bludgeoning", "Slashing", "Fire", "Cold", "Lightning", "Radiant",
    "Necrotic", "Psychic", "Force", "Elemental", "Lightning", "Thunder", "Acid",
    "Poison", "Slashing",
])

class DamageDealer:
    def __init__(self, name, damage, damage_type reach=None, range=None):
        self.__name = name
        # Range in feets, implies a ranged attack. None if can't make ranged attacks.
        # self.__range = range
        # Reach in feets, implies a meele attack. None if can't make meele attacks.
        # self.__reach = reach
        self.__attack
        self.__damage_type
        self.__damage = damage
