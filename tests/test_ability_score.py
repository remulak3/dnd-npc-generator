from ability_score import AbilityScores

def test_calculate_ability_bonus_neutral():
    assert AbilityScores.calculate_ability_bonus(10) == "0"

def test_calculate_ability_bonus_negative():
    assert AbilityScores.calculate_ability_bonus(8) == "-1"

def test_calculate_ability_bonus_positive():
    assert AbilityScores.calculate_ability_bonus(18) == "+4"

def test_generate_ability_scores_has_table_values():
    test_scores = AbilityScores()
    assert 8,10 in test_scores.scores.values()
    assert 12,13 in test_scores.scores.values()
    assert 15 in test_scores.scores.values()
    