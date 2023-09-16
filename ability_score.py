import random

class AbilityScores():
    scores = {}
    scores["strength"] = 10
    scores["intelligence"] = 10
    scores["charisma"] = 10
    scores["wisdom"] = 10
    scores["dexterity"] = 10
    scores["constitution"] = 10

    def __init__(self):
        self.scores = {}
        self.generate_ability_scores()
    
    def generate_ability_scores(self):
        array_values = [15, 14, 13, 12, 10, 8]
        random.shuffle(array_values)
        self.scores["strength"] = array_values[0]
        self.scores["intelligence"] = array_values[1]
        self.scores["charisma"] = array_values[2]
        self.scores["wisdom"] = array_values[3]
        self.scores["dexterity"] = array_values[4]
        self.scores["constitution"] = array_values[5]
    