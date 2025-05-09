from gear.holdable.holdable import Holdable
from damage_dealing import Attack, Damage, DamageType
from service import Ability
from die import DieRoll, d4


class Weapon(Holdable, Attack):
    def __init__(
        self,
        name: str,
        ability: Ability,
        damages: list[Damage],
        two_handed = False,
        versatile = False,
        ):
            Holdable.__init__(self, two_handed=two_handed, versatile=versatile)
            Attack.__init__(self, ability).add_damages(damages)
            return self


    def get_ability(self):
        return self.__ability


    def set_ability_val(self, ability_val):


class Melee(Weapon):
    def __init__(
        self,
        name: str,
        damages: list[Damage],
        finess = False,
        two_handed = False,
        versatile = False,
        reach = 5,
        ):
            Weapon.__init__(self, name, Ability.DEX if finess else Ability.STR, damages, two_handed, versatile)
            return self


Fist = Melee("Fist", [Damage(d4, DamageType.Bludgeoning)])


# class Ranged(Weapon):
#     def __init__(
#         self,
#         name: str,
#         optimal_range,
#         max_range,
#         two_handed = False,
#         versatile = False,
#         ):
