from race import Race

Dwarf = Race()
Dwarf.name = "Dwarf"
Dwarf.size = "Medium"
Dwarf.speed = 25
Dwarf.darkvision = 60
Dwarf.languages.append("Dwarvish")
Dwarf.ability_score_improvement_by_2["constitution"] = 2
Dwarf.abilities[
    "Dwarven Resilience"
] = """You have advantage on saving throws against poison,
    and you have resistance against poison damage."""
Dwarf.abilities[
    "Dwarven Combat Training"
] = "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
Dwarf.abilities[
    "Tool Proficiency"
] = """You gain proficiency with the artisan’s tools of your choice: smith’s tools,
    brewer’s supplies, or mason’s tools."""
Dwarf.abilities[
    "Stonecunning"
] = """Whenever you make an Intelligence (History) check related to the origin of stonework,
    you are considered proficient in the History skill and add double your proficiency bonus to the check,
    instead of your normal proficiency bonus"""
