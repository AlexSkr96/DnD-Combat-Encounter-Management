from gear.holdable.holdable import Holdable
from damage_dealing import Attack
from service import Ability


class Weapon(Holdable, Attack):
    def __init__(
        self,
        name: str,
        ability: Ability,
        two_handed = False,
        versatile = False,
        ):
            Holdable.__init__(self, two_handed=two_handed, versatile=versatile)
            Attack.__init__(self, ability)


class Melee(Weapon):
    def __init__(
        self,
        name: str,
        finess = False,
        two_handed = False,
        versatile = False,
        reach = 5,
        ):
            Weapon.__init__(self, name, Ability.DEX if finess else Ability.STR, two_handed, versatile)


class Ranged(Weapon):
    def __init__(
        self,
        name: str,
        optimal_range,
        max_range,
        two_handed = False,
        versatile = False,
        ):
