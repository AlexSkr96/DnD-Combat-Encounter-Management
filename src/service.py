from enum import Enum


Ability = Enum("Ability", ["STR", "INT", "DEX", "WIS", "CON", "CHA"])
Skill = Enum("Skill",
    [
        "Acrobatics", "Animal_handling", "Arcana", "Athletics", "Deception",
        "History", "Insight", "Intimidation", "Investigation", "Medicine",
        "Nature", "Perception", "Performance", "Persuasion", "Religion",
        "Sleight_of_hand", "Stealth", "Survival"
    ]
)
# Dict to determine base ability of a skill
Skill_to_ability = {
    Skill.Acrobatics: Ability.DEX,
    Skill.Animal_handling: Ability.WIS,
    Skill.Arcana: Ability.INT,
    Skill.Athletics: Ability.STR,
    Skill.Deception: Ability.CHA,
    Skill.History: Ability.INT,
    Skill.Insight: Ability.WIS,
    Skill.Intimidation: Ability.CHA,
    Skill.Investigation: Ability.INT,
    Skill.Medicine: Ability.WIS,
    Skill.Nature: Ability.INT,
    Skill.Perception: Ability.WIS,
    Skill.Performance: Ability.CHA,
    Skill.Persuasion: Ability.CHA,
    Skill.Religion: Ability.INT,
    Skill.Sleight_of_hand: Ability.DEX,
    Skill.Stealth: Ability.DEX,
    Skill.Survival: Ability.WIS
}
