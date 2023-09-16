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
        
    @staticmethod
    def calculate_ability_bonus(value) -> str:
        if value == 1:
            return "-5"
        if value in range(2,4):
            return "-4"
        if value in range(4,6):
            return "-3"
        if value in range(6,8):
            return "-2"
        if value in range(8,10):
            return "-1"
        if value in range(10,12):
            return "0"
        if value in range(12,14):
            return "+1"
        if value in range(14,16):
            return "+2"
        if value in range(16,18):
            return "+3"
        if value in range(18,20):
            return "+4"
        if value in range(20,22):
            return "+5"
        if value in range(22,24):
            return "+6"
        if value in range(24,26):
            return "+7"
        if value in range(26,28):
            return "+8"
        if value in range(28,30):
            return "+9"
        if value >= 30:
            return "+10"

    def print_ability_scores_bonuses(self):
        for name, value in self.scores.items():
            print(name,":",value,"(",AbilityScores.calculate_ability_bonus(value),")")

    def pick_random_ability_score(self):
        ability_scores = self.scores.keys()
        return random.choice(ability_scores)
