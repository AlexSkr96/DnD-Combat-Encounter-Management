from service import Ability
from die import Die


class Character:
    def __init__(
        self,
        name: str,
        hp: int,
        ac: int,
        speed: int,
        strength: int,
        intelligence: int,
        dexterity: int,
        wisdow: int,
        constitution: int,
        charisma: int,
    ):
        self.__name = None

        self.__max_hp = None
        self.hp = None
        self.temp_hp = None
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

        self.__abilities = {}
        for ability in Ability:
            self.__abilities[ability] = None

        self.__skills = {}

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action


    def attack(self, target: Character):
