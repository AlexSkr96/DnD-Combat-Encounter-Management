from service import Ability, Skill, Skill_to_ability
from die import Die


class Character:
    def __init__(
        self,
        name: str,
        speed: int,
        strength: int,
        intelligence: int,
        dexterity: int,
        wisdom: int,
        constitution: int,
        charisma: int,
        hp: int,
    ):
        self.__name = name

        self.__max_hp = hp
        self.hp = hp
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
            Ability.STR: strength,
            Ability.DEX: dexterity,
            Ability.CON: constitution,
            Ability.INT: intelligence,
            Ability.WIS: wisdom,
            Ability.CHA: charisma
        }

        # self.__skills = {}

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action


    def attack(self, target: Character):
