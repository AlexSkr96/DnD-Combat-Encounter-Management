from random import randint


class Die:
    def __init__(self, sides):
        self.__sides = sides

    def roll(self):
        return randint(1, self.__sides)

    def get_num_sides(self):
        return self.__sides

    def get_die_roll(self, number_of_dice = 1, modifier = 0):
        return DieRoll(self.__sides, number_of_dice, modifier)


d4 =  Die(4)
d6 =  Die(6)
d8 =  Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)

def roll_ability():
    rolls = []
    for _ in range(4):
        rolls.append(d6.roll())

    rolls.remove(min(rolls))
    return sum(rolls)


class DieRoll(Die):
    def __init__(self, sides, number_of_dice = 1, modifier = 0):
        super().__init__(sides)
        self.__number_of_dice = number_of_dice
        self.__modifier = modifier

    def roll(self):
        res = self.__modifier
        for _ in range(self.__number_of_dice):
            res += randint(1, self.get_num_sides())

        return res
