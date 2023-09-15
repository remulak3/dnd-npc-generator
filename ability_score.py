import random

class AbilityScores():
    strength = 10
    intelligence = 10
    charisma = 10
    wisdom = 10
    dexterity = 10
    constitution = 10

    def __init__(self):
        pass
    
    def generate_ability_scores(self):
        array_values = [15, 14, 13, 12, 10, 8]
        random.shuffle(array_values)
        self.strength = array_values[0]
        self.intelligence = array_values[1]
        self.charisma = array_values[2]
        self.wisdom = array_values[3]
        self.dexterity = array_values[4]
        self.constitution = array_values[5]        
    