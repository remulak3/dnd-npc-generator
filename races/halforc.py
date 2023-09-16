from race import Race

HalfOrc = Race()
HalfOrc.name = "HalfOrc"
HalfOrc.size = "Medium"
HalfOrc.speed = 30
HalfOrc.darkvision = 60
HalfOrc.languages.append("Orc")
HalfOrc.ability_score_improvement_by_2["strength"] = 2
HalfOrc.ability_score_improvement_by_1["constitution"] = 1

HalfOrc.abilities["Menacing"] = "You gain proficiency in the Intimidation skill."
HalfOrc.abilities[
    "Relentless Endurance"
] = """When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit
    point instead. You can’t use this feature again until you finish a long rest."""
HalfOrc.abilities[
    "Savage Attacks"
] = """When you score a critical hit with a melee weapon attack, you can roll one of the
    weapon’s damage dice one additional time and add it to the extra damage of the critical hit."""
