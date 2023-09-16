from race import Race

Gnome = Race()
Gnome.name = "Gnome"
Gnome.size = "Small"
Gnome.speed = 25
Gnome.darkvision = 60
Gnome.languages.append("Gnomish")
Gnome.ability_score_improvement_by_2["intelligence"] = 2
Gnome.abilities["Keen Senses"] = "You have proficiency in the Perception skill."
Gnome.abilities[
    "Gnome Cunning"
] = "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
