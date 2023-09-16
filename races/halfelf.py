from race import Race
from ability_score import AbilityScores

HalfElf = Race()
HalfElf.name = "HalfElf"
HalfElf.size = "Medium"
HalfElf.speed = 30
HalfElf.darkvision = 60
HalfElf.languages.append("Elvish")
HalfElf.languages.append("One extra language of your choice")
HalfElf.ability_score_improvement_by_2["charisma"] = 2
HalfElf.ability_score_improvement_by_1[AbilityScores().pick_random_ability_score()] = 1
HalfElf.ability_score_improvement_by_1[AbilityScores().pick_random_ability_score()] = 1

HalfElf.abilities["Keen Senses"] = "You have proficiency in the Perception skill."
HalfElf.abilities[
    "Fey Ancestry"
] = "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
HalfElf.abilities[
    "Skill Versatility"
] = """You gain proficiency in two skills of your choice."""
