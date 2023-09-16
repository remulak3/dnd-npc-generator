from ability_score import AbilityScores

def test_calculate_ability_bonus_neutral():
    assert AbilityScores.calculate_ability_bonus(10) == "0"

def test_calculate_ability_bonus_negative():
    assert AbilityScores.calculate_ability_bonus(8) == "-1"

def test_calculate_ability_bonus_positive():
    assert AbilityScores.calculate_ability_bonus(18) == "+4"