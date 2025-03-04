from die import *
from service import *
from character.character import Character, Size, Type


dolgrim = Character(
    "dolgrim",
    strength=15,
    intelligence=8,
    dexterity=14,
    wisdom=10,
    constitution=12,
    charisma=8,
    hp=d6.get_die_roll(3, 3),
    size=Size.Small,
    type=Type.Aberration,
    natural_armour=11
)
print(dolgrim)

jamy = Character(
    "Jamy",
    hp=25,
    size=Size.Medium,
    type=Type.Humanoid
)
print(jamy)
