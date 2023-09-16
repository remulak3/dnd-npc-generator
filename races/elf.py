from race import Race

Elf = Race()
Elf.name = "Elf"
Elf.size = "Medium"
Elf.speed = 30
Elf.darkvision = 60
Elf.languages.append("Elvish")
Elf.ability_score_improvement_by_2["dexterity"] = 2
Elf.abilities["Keen Senses"] = "You have proficiency in the Perception skill."
Elf.abilities["Fey Ancestry"] = "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
Elf.abilities["Trance"] = "YElves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."
Elf.abilities["Stonecunning"] = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus"
