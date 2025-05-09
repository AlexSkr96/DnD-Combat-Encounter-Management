from enum import Enum

from service import Ability
from die import *
from character.character import Character


DamageType = Enum("Damage Type", [
    "Piercing", "Bludgeoning", "Slashing", "Fire", "Cold", "Lightning", "Radiant",
    "Necrotic", "Psychic", "Force", "Elemental", "Lightning", "Thunder", "Acid",
    "Poison", "Slashing",
])


class Damage:
    def __init__(self, damage_dice: Die, damage_type: DamageType):
        self.__damage_type = damage_type
        self.__damage_dice = damage_dice
        return self

    def deal(self):
        return self.__damage_dice.roll(), self.__damage_type


class Attack:
    def __init__(self, ability: Ability):
        self.__ability = ability
        self.__attack_die = d20
        self.__damages = []
        return self

    def add_damage(self, damage: Damage):
        self.__damages.append(damage)

    def add_damages(self, damage: list[Damage]):
        for damage in self.__damages:
            self.__damages.append(damage)

    def target(self, target: Character):
        attack_roll = self.__attack_die.roll()
        if attack_roll > target.get_ac():
            for damage in self.__damages:
                target.get_damaged(damage.deal())
