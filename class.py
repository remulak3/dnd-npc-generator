class Class:
    def __init__(self) -> None:
        self.name = ""
        self.hit_dice = 0
        self.level = 1
        self.starting_hit_points = 0
        self.hitpoints = self.starting_hit_points
        self.armor_proficiencies = []
        self.weapon_proficiencies = []
        self.tools_proficiences = []
        self.saving_throws_proficiencies = []
        self.skill_proficiencies = []
        self.starting_equipment = {}
        self.class_abilities = {}

    def describe_class(self):
        print("Class: ", self.name)
        print("Level:", self.level)
        print("Hit die: ", self.hit_dice)
        print("Hitpoints: ", self.hitpoints)
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
            for name, description in self.starting_equipment.items():
                print(" - ", name, ":", description)
        for ability_name, ability_description in self.class_abilities.items():
            print(" - ", ability_name, ":", ability_description)
