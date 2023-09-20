import random


class NpcClass:
    def __init__(self, level=1) -> None:
        self.name = ""
        self.hit_dice = 0
        self.level = level if level > 1 else 1
        self.starting_hit_points = 0
        self.armor_proficiencies = []
        self.weapon_proficiencies = []
        self.tools_proficiences = []
        self.saving_throws_proficiencies = []
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.class_abilities = {}
        self.subclass = ""

    def describe_class(self):
        print("Class: ", self.name)
        print("Level:", self.level)
        print("Hit die: ", self.hit_dice)
        print("Armor Proficiencies:")
        for proficiency in self.armor_proficiencies:
            print("-", proficiency)
        print("Weapon Proficiencies:")
        for proficiency in self.weapon_proficiencies:
            print("-", proficiency)
        print("Tools Proficiencies:")
        for proficiency in self.tools_proficiences:
            print("-", proficiency)
        print("Saving Throws Proficiencies")
        for proficiency in self.saving_throws_proficiencies:
            print("-", proficiency)
        print("Skill Proficiencies")
        for proficiency in self.skill_proficiencies:
            print("-", proficiency)
        if len(self.starting_equipment) > 0:
            print("Equipment:")
            for item in self.starting_equipment:
                print("-", item)
        for ability_name, ability_description in self.class_abilities.items():
            print(" - ", ability_name, ":", ability_description)

    @staticmethod
    def pick_x_random_skills(count, list_of_skills):
        chosen_skills = []
        random.shuffle(list_of_skills)
        for i in range(count):
            chosen_skills.append(list_of_skills[i])
        return chosen_skills
