from service import Ability, Skill, Skill_to_ability
from die import *


class Character:
    def __init__(
        self,
        name: str,
        hp: int | Die,
        strength: int = -1,
        intelligence: int = -1,
        dexterity: int = -1,
        wisdom: int = -1,
        constitution: int = -1,
        charisma: int = -1,
        # lvl: int = 1,
        speed: int = 30,
    ):
        self.__name = name

        if isinstance(hp, Die):
            self.__max_hp = hp.roll()
        else:
            self.__max_hp = hp

        self.hp = self.__max_hp
        self.temp_hp = 0

        self.__ac = None
        self.__speed = None
        self.__initiative = None

        self.__inspiration = False
        self.__proficiency_bonus = None
        self.__proficiencies = {
            "saving_throws": [],
            "skills": [],
            "gear": []
        }

        self.__abilities = {
            Ability.STR: strength if strength > -1 else roll_ability(),
            Ability.DEX: dexterity if dexterity > -1 else roll_ability(),
            Ability.CON: constitution if constitution > -1 else roll_ability(),
            Ability.INT: intelligence if intelligence > -1 else roll_ability(),
            Ability.WIS: wisdom if wisdom > -1 else roll_ability(),
            Ability.CHA: charisma if charisma > -1 else roll_ability()
        }

        # self.__skills = {}

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action


    def __repr__(self):
        repr = f"=== {self.__name} ===\n"
        for ability in self.__abilities:
            ability_value = self.__abilities[ability]
            ability_modifier = self.get_ability_mod(ability)
            repr += f"{str(ability)[-3:]}: {ability_modifier} ({ability_value}) | "

        return repr


    def get_ability_mod(self, ability: Ability):
        return (self.__abilities[ability] - 10) // 2


    def get_skill_mod(self, skill: Skill):
        ability = Skill_to_ability[skill]
        return self.get_ability_mod(ability)



    # def attack(self, target: Character):
