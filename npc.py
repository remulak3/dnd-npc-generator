import random
from ability_score import AbilityScores
from races.dwarf import Dwarf
from races.human import Human
from races.elf import Elf
from races.halfling import Halfling
from races.dragonborn import Dragonborn
from races.gnome import Gnome
from races.halfelf import HalfElf
from races.halforc import HalfOrc
from races.tiefling import Tiefling
from classes.barbarian import Barbarian


class Npc:
    ability_scores = AbilityScores()

    def __init__(self) -> None:
        self.race = {}
        self.npc_class = {}
        self.hitpoints = 0
        self.generate_race()
        self.apply_race_asi()
        self.armor_class = 10 + int(
            AbilityScores.calculate_ability_bonus(
                self.ability_scores.scores["dexterity"]
            )
        )
        self.generate_class()
        self.setup_hitpoints()

    def generate_race(self):
        available_races = [
            Dwarf,
            Human,
            Elf,
            Halfling,
            Dragonborn,
            Gnome,
            HalfElf,
            HalfOrc,
            Tiefling,
        ]
        self.race = random.choice(available_races)

    def generate_class(self):
        available_classes = [Barbarian]
        self.npc_class = random.choice(available_classes)

    def setup_hitpoints(self):
        self.hitpoints = self.npc_class.starting_hit_points + int(
            AbilityScores.calculate_ability_bonus(
                self.ability_scores.scores["constitution"]
            )
        )

    def print_statblock(self) -> None:
        for name, value in self.ability_scores.scores.items():
            print(name, ":", value)

    def print_npc_info(self) -> None:
        self.ability_scores.print_ability_scores_bonuses()
        self.describe_npc_properties()
        self.race.describe_race()
        self.npc_class.describe_class()

    def describe_npc_properties(self) -> None:
        print("Armor Class: ", self.armor_class)
        print("Hitpoints: ", self.hitpoints)

    def apply_race_asi(self) -> None:
        for name, value in self.race.ability_score_improvement_by_2.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
        for name, value in self.race.ability_score_improvement_by_1.items():
            self.ability_scores.scores[name] = self.ability_scores.scores[name] + value
