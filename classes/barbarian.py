from npc_class import NpcClass
import random


def create_barbarian(level=1) -> NpcClass:
    Barbarian = NpcClass(level)
    Barbarian.name = "Barbarian"
    Barbarian.hit_dice = 12
    Barbarian.starting_hit_points = 12

    Barbarian.armor_proficiencies.append("light armor")
    Barbarian.armor_proficiencies.append("medium armor")
    Barbarian.armor_proficiencies.append("shields")

    Barbarian.weapon_proficiencies.append("simple weapons")
    Barbarian.weapon_proficiencies.append("martial weapons")

    Barbarian.tools_proficiences.append("none")

    Barbarian.saving_throws_proficiencies.append("strength")
    Barbarian.saving_throws_proficiencies.append("constitution")

    available_skills = [
        "Animal Handling",
        "Athletics",
        "Intimidation",
        "Nature",
        "Perception",
        "Survival",
    ]
    Barbarian.skill_proficiencies.extend(
        NpcClass.pick_x_random_skills(2, available_skills)
    )

    available_equipment_1 = ["(a) a greataxe", "(b) any martial melee weapon"]
    Barbarian.starting_equipment.append(random.choice(available_equipment_1))
    available_equipment_2 = ["(a) two handaxes", "(b) any simple weapon"]
    Barbarian.starting_equipment.append(random.choice(available_equipment_2))
    Barbarian.starting_equipment.append("An explorer’s pack and four javelins")

    Barbarian.class_abilities[
        "Rage"
    ] = """
    In battle, you fight with primal ferocity. On your turn, you can enter a rage
    as a bonus action.

    While raging, you gain the following benefits if you aren’t wearing heavy
    armor:
    -You have advantage on Strength checks and Strength saving throws.
    -When you make a melee weapon attack using Strength, you gain a bonus to the
    damage roll that increases as you gain levels as a barbarian, as shown in
    the Rage Damage column of the Barbarian table.
    -You have resistance to bludgeoning, piercing, and slashing damage.

    If you are able to cast spells, you can’t cast them or concentrate on them
    while raging.

    Your rage lasts for 1 minute. It ends early if you are knocked unconscious or
    if your turn ends and you haven’t attacked a hostile creature since your last
    turn or taken damage since then. You can also end your rage on your turn as a
    bonus action.

    Once you have raged the number of times shown for your barbarian level in the
    Rages column of the Barbarian table, you must finish a long rest before you
    can rage again.
    """
    Barbarian.class_abilities[
        "Unarmored Defense"
    ] = """
    While you are not wearing any armor, your Armor Class equals 10 + your
    Dexterity modifier + your Constitution modifier. You can use a shield and
    still gain this benefit.
    """

    if Barbarian.level >= 2:
        Barbarian.class_abilities[
            "Reckless Attack"
        ] = """
        Starting at 2nd level, you can throw aside all concern for defense to
        attack with fierce desperation. When you make your first attack on your
        turn, you can decide to attack recklessly. Doing so gives you advantage on
        melee weapon attack rolls using Strength during this turn, but attack
        rolls against you have advantage until your next turn.
        """
        Barbarian.class_abilities[
            "Danger Sense"
        ] = """
        At 2nd level, you gain an uncanny sense of when things nearby aren’t as
        they should be, giving you an edge when you dodge away from danger.

        You have advantage on Dexterity saving throws against effects that you can
        see, such as traps and spells. To gain this benefit, you can’t be blinded,
        deafened, or incapacitated.
        """

    return Barbarian
