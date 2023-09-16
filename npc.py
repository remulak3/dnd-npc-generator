import random
from ability_score import AbilityScores
from races.dwarf import Dwarf
from races.human import Human
from races.elf import Elf
from races.halfling import Halfling
from races.dragonborn import Dragonborn
from races.gnome import Gnome
from races.halfelf import HalfElf


class Npc:
    ability_scores = AbilityScores()

    def __init__(self) -> None:
        self.race = {}
        self.generate_race()
        self.apply_race_asi()

    def generate_race(self):
        available_races = [Dwarf, Human, Elf, Halfling, Dragonborn, Gnome, HalfElf]
        self.race = random.choice(available_races)

    def print_statblock(self) -> None:
        for name, value in self.ability_scores.scores.items():
            print(name, ":", value)

    def print_npc_info(self) -> None:
        self.ability_scores.print_ability_scores_bonuses()
        self.race.describe_race()

    def apply_race_asi(self) -> None:
        for name, value in self.race.ability_score_improvement_by_2.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
        for name, value in self.race.ability_score_improvement_by_1.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
