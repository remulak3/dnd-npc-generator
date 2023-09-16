from race import Race

Halfling = Race()
Halfling.name = "Halfling"
Halfling.size = "Small"
Halfling.speed = 25
Halfling.darkvision = 0
Halfling.languages.append("Halfling")
Halfling.ability_score_improvement_by_2["dexterity"] = 2
Halfling.abilities[
    "Lucky"
] = """When you roll a 1 on the d20 for an attack roll, ability check, or saving throw,
    you can reroll the die and must use the new roll."""
Halfling.abilities[
    "Brave"
] = "You have advantage on saving throws against being frightened."
Halfling.abilities[
    "Halfling Nimbleness."
] = "You can move through the space of any creature that is of a size larger than yours."
