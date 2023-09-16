

class Race:
    def __init__(self) -> None:
        self.name = ""
        self.size = ""
        self.speed = 0
        self.darkvision = 0
        self.languages = ["common"]
        self.ability_score_improvement_by_1 = {}
        self.ability_score_improvement_by_2 = {}
        self.abilities = {}

    def describe_race(self):
        print("Race: ",self.name)
        print("Size: ",self.size)
        print("Speed: ",self.speed,"ft")
        if self.darkvision > 0:
            print("Darkvision: ",self.darkvision,"ft")
        print("Languages:")
        for language in self.languages:
            print("-", language)
        if len(self.abilities) > 0:
            print("Abilities:")
            for name, description in self.abilities.items():
                print(" - ",name,": ", description)
