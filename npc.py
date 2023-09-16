import random
from ability_score import AbilityScores
from race import Race
from races.dwarf import Dwarf
from races.human import Human

class Npc:
    ability_scores = AbilityScores()
    race = Race()
    def __init__(self) -> None:
        self.generate_race()
        self.apply_race_asi()

    def generate_race(self):
        available_races = [
            Dwarf,
            Human
        ]
        print(random.choice(available_races).name)
        self.race = random.choice(available_races)

    def print_statblock(self) -> None:
        for name, value in self.ability_scores.scores.items():
            print(name,":",value)
    
    def print_npc_info(self) -> None:
        self.ability_scores.print_ability_scores_bonuses()
        self.race.describe_race()

    def apply_race_asi(self) -> None:
        for name, value in self.race.ability_score_improvement_by_2.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
        for name, value in self.race.ability_score_improvement_by_1.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
