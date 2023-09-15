from ability_score import AbilityScores
from race import Race
class Npc:
    ability_scores = AbilityScores()
    race = Race()
    def __init__(self) -> None:
        self.ability_scores.generate_ability_scores()

    def print_statblock(self) -> None:
        print('STR: ',self.ability_scores.strength)
        print('CHR: ',self.ability_scores.charisma)
        print('INT: ',self.ability_scores.intelligence)
        print('WIS: ',self.ability_scores.wisdom)
        print('CON: ',self.ability_scores.constitution)
        print('DEX: ',self.ability_scores.dexterity)
