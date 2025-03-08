from holdable.holdable import Holdable
from damage_dealing import Attack


class Weapon(Holdable, Attack):
    def __init__(
        self,
        two_handed = False,
        versatile = False
    ):
        Holdable.__init__(self, two_handed=two_handed, versatile=versatile)
