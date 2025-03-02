from die import *
from service import *
from character import Character


dolgrim = Character(
    "dolgrim",
    strength=15,
    intelligence=8,
    dexterity=14,
    wisdom=10,
    constitution=12,
    charisma=8,
    hp=d6.get_die_roll(3, 3)
)

jamy = Character(
    "Jamy",
    hp = 25
)
print(jamy)
print(jamy.get_skill_mod(Skill.Arcana))
