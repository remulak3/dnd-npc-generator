from race import Race

Tiefling = Race()
Tiefling.name = "Tiefling"
Tiefling.size = "Medium"
Tiefling.speed = 30
Tiefling.darkvision = 60
Tiefling.languages.append("Infernal")
Tiefling.ability_score_improvement_by_2["charisma"] = 2
Tiefling.ability_score_improvement_by_1["intelligence"] = 1
Tiefling.abilities[
    "Hellish Resistance"
] = """You have resistance to fire damage."""
Tiefling.abilities[
    "Infernal Legacy"
] = """You know the thaumaturgy cantrip. When you reach 3rd level, you can cast
    the hellish rebuke spell as a 2nd-level spell once with this trait and regain
    the ability to do so when you finish a long rest. When you reach 5th level,
    you can cast the darkness spell once with this trait and regain the ability
    to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."""
