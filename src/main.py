from die import *
from service import Ability


print(d20.roll())

d6x2 = d6.get_die_roll(2)
print(d6x2.roll())


for i in Ability:
    print(i)
