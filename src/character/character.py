from enum import Enum

from errors import GearSlotOccupiedException, InsuficcientAPException
from gear.holdable.shield import Shield
from gear.wearable.wearable import Wearable
from gear.holdable.holdable import Holdable
from gear.holdable.weapon import Weapon
from service import Ability, Skill, Skill_to_ability
from die import *


class Type(Enum):
    Aberration = 1
    Beast = 2
    Celestial = 3
    Construct = 4
    Dragon = 5
    Elemental = 6
    Fey = 7
    Fiend = 8
    Giant = 9
    Humanoid = 10
    Monstrosity = 11
    Ooze = 12
    Plant = 13
    Undead = 14

class Size(Enum):
    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4
    Huge = 5
    Gargantuan = 6

# Alignment by lawfulness
class LAlignment(Enum):
    Lawful = 1
    Neutral = 2
    Chaotic = 3

# Alignment by goodness
class GAlignment(Enum):
    Good = 1
    Neutral = 2
    Evil = 3


class State(Enum):
    Alive = 1
    Dead = 2
    Incapacitated = 3


class Character:
    def get_ability_mod(self, ability: Ability):
        return (self.__abilities[ability] - 10) // 2


    def get_skill_mod(self, skill: Skill):
        ability = Skill_to_ability[skill]
        return self.get_ability_mod(ability)


    def get_ac(self):
        #TODO: implement armour
        return 10 + self.get_ability_mod(Ability.DEX)


    def __init__(
        self,
        name: str,
        hp: int | Die,
        type: Type,
        size: Size,
        lawfulness: LAlignment | None = None,
        goodness: GAlignment | None = None,
        strength: int = -1,
        intelligence: int = -1,
        dexterity: int = -1,
        wisdom: int = -1,
        constitution: int = -1,
        charisma: int = -1,
        # lvl: int = 1,
        speed: int = 30,
        natural_armour: int = 10,
    ):
        self.__name = name

        if isinstance(hp, Die):
            self.__max_hp = hp.roll()
        else:
            self.__max_hp = hp

        self.__hp = self.__max_hp
        self.__temp_hp = 0

        self.__speed = speed
        self.__initiative = None
        self.__size = size
        self.__lawfulness = lawfulness
        self.__goodness = goodness
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

        self.__ac = natural_armour + self.get_ability_mod(Ability.DEX)
        # self.__skills = {}

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action
        self.__action = 1
        self.__bonus_action = 1
        self.__reaction = 1

        self.__hand = Weapon.fist # What characters holds in primary hand
        self.__off_hand = None # What character holds in secondary hand

        self.__combat_mode = False # Character needs to use actions while in combat mode

        self.__state = State.Alive


    def __repr__(self):
        repr = f"=== {self.__name} ===\n"
        repr += f"♥️ {self.__hp}/{self.__max_hp}"
        if self.__temp_hp != 0:
            repr += f"+{self.__temp_hp}"
        repr += f" ♥️\n⛨ {self.__ac} ⛨\n"

        for ability in self.__abilities:
            ability_value = self.__abilities[ability]
            ability_modifier = self.get_ability_mod(ability)
            repr += f"{str(ability)[-3:]}: {ability_modifier} ({ability_value}) | "

        return repr

    def get_damaged(self, damage):
        self.__hp -= damage
        if self.__hp < -10:
            self.die()
        elif self.__hp <= 0:
            self.get_incapacitated()


    def equip_weapon(self, weapon: Weapon):
        weapon.set_ability_val(self.__abilities[weapon.get_ability()])


    def roll_initiative(self):
        return d20.roll() + self.get_ability_mod(Ability.DEX)


    # Decorator function to be used for actions that require an action point
    def use_action(self, action):
        def wrapper(*args, **kwargs):
            if self.__action < 1:
                raise InsuficcientAPException()
            else:
                self.__action -= 1
                return action(*args, **kwargs)

        return wrapper


    # def use_bonus_action(self, action):
    #     if self.__bonus_action < 1:
    #         raise InsuficcientAPException()
    #     else:
    #         self.__bonus_action -= 1


    # def use_reaction(self):
    #     if self.__reaction < 1:
    #         raise InsuficcientAPException()
    #     else:
    #         self.__reaction -= 1


    def die(self):
        self.__state = State.Dead


    def get_incapacitated(self):
        self.__state = State.Incapacitated
        self.__fails = 0
        self.__successes = 0


    def roll_death_save(self):
        if self.__state != State.Incapacitated:
            raise Exception("Character is not incapacitated")

        roll = d20.roll()
        mod = 2 if roll in [1, 20] else 1
        if roll > 10:
            self.__successes += mod
        else:
            self.__fails += mod

        if self.__fails >= 3:
            self.die()
        else:
            self.__fails = None
            self.__successes = None
            self.__hp = 1
            self.__state = State.Alive


    def equip_holdable(self, gear: Holdable, how = "Auto"):
        if how == "Auto":
            if not self.__hand and not isinstance(gear, Shield):
                self.__hand = Holdable
            elif not self.__off_hand:
                self.__off_hand = Holdable
        elif how == "Primary":
            if not self.__hand:
                self.__hand = gear
        elif how == "Secondary":
            if not self.__off_hand:
                self.__off_hand = gear
        elif how == "Two-handed":
            if not (self.__hand or self.__off_hand):
                self.__hand = gear
                self.__off_hand = self.__off_hand

        raise GearSlotOccupiedException()



    # def unequip_holdable(self):

    @Character.use_action
    def attack(self, target: Character):
        self.__hand.attack(target)


    def start_turn(self, enemies: list[Character], allies: list[Character] = []):
        # movement = self.__speed
        self.__action = 1
        self.__bonus_action = 1
        self.__reaction = 1

        # print(f"What would you like to do, {self.__name}?")
        print(f"Who would you like to attack, {self.__name}?")
        for i in range(1, len(enemies)+1):
            print(f"{i}. {enemies[i].get_name} {enemies[i].het_pretty_health}")
