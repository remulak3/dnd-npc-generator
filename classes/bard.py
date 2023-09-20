from npc_class import NpcClass
import random
from enum import Enum, auto


class college(Enum):
    CollegeOfLore = auto()
    CollegeOfValor = auto()


def create_bard(level=1) -> NpcClass:
    Bard = NpcClass(level)
    Bard.name = "Bard"
    Bard.hit_dice = 8
    Bard.starting_hit_points = 8

    Bard.armor_proficiencies.append("light armor")

    Bard.weapon_proficiencies.append("simple weapons")
    Bard.weapon_proficiencies.append("hand crossbows")
    Bard.weapon_proficiencies.append("longswords")
    Bard.weapon_proficiencies.append("rapiers")
    Bard.weapon_proficiencies.append("shortswords")

    Bard.tools_proficiences.append("Three musical instruments of your choice")

    Bard.saving_throws_proficiencies.append("dexterity")
    Bard.saving_throws_proficiencies.append("charisma")

    available_skills = [
        "Athletics",
        "Acrobatics",
        "Sleight of Hand",
        "Stealth",
        "Arcana",
        "History",
        "Investigation",
        "Nature",
        "Religion",
        "Animal Handling",
        "Insight",
        "Medicine",
        "Perception",
        "Survival",
        "Deception",
        "Intimidation",
        "Performance",
        "Persuasion",
    ]
    Bard.skill_proficiencies.extend(NpcClass.pick_x_random_skills(3, available_skills))

    available_equipment_1 = ["(a) a rapier", "(b) a longsword", "(c) any simple weapon"]
    Bard.starting_equipment.append(random.choice(available_equipment_1))
    available_equipment_2 = ["(a) a diplomat's pack", "(b) an entertainer's pack"]
    Bard.starting_equipment.append(random.choice(available_equipment_2))
    available_equipment_3 = ["(a) a lute", "(b) any other musical instrument"]
    Bard.starting_equipment.append(random.choice(available_equipment_3))
    Bard.starting_equipment.append("Leather armor and a dagger")

    Bard.class_abilities[
        "Spellcasting"
    ] = """
    You have learned to untangle and reshape the fabric of reality in harmony
    with your wishes and music. Your spells are part of your vast repertoire,
    magic that you can tune to different situations. See chapter 10 for the
    general rules of spellcasting and chapter 11 for the bard spell list.

    Cantrips You know two cantrips of your choice from the bard spell list. You
    learn additional bard cantrips of your choice at higher levels, as shown in
    the Cantrips Known column of the Bard table.

    Spell Slots The Bard table shows how many spell slots you have to cast your
    bard spells of 1st level and higher. To cast one of these spells, you must
    expend a slot of the spell’s level or higher. You regain all expended spell
    slots when you finish a long rest.

    For example, if you know the 1st-level spell cure wounds and have a
    1st-level and a 2nd-level spell slot available, you can cast cure wounds
    using either slot.

    Spells Known of 1st Level and Higher You know four 1st-level spells of your
    choice from the bard spell list.

    The Spells Known column of the Bard table shows when you learn more bard
    spells of your choice. Each of these spells must be of a level for which
    you have spell slots, as shown on the table. For instance, when you reach
    3rd level in this class, you can learn one new spell of 1st or 2nd level.

    Additionally, when you gain a level in this class, you can choose one of
    the bard spells you know and replace it with another spell from the bard
    spell list, which also must be of a level for which you have spell slots.

    Spellcasting Ability Charisma is your spellcasting ability for your bard
    spells. Your magic comes from the heart and soul you pour into the
    performance of your music or oration. You use your Charisma whenever a
    spell refers to your spellcasting ability. In addition, you use your
    Charisma modifier when setting the saving throw DC for a bard spell you
    cast and when making an attack roll with one.

    Spell save DC = 8 + your proficiency bonus + your Charisma modifier

    Spell attack modifier = your proficiency bonus + your Charisma modifier

    Ritual Casting You can cast any bard spell you know as a ritual if that
    spell has the ritual tag.

    Spellcasting Focus You can use a musical instrument (see chapter 5,
    “Equip­ment”) as a spellcasting focus for your bard spells.
    """
    Bard.class_abilities[
        "Bardic Inspiration"
    ] = """
    You can inspire others through stirring words or music. To do so, you use a
    bonus action on your turn to choose one creature other than yourself within
    60 feet of you who can hear you. That creature gains one Bardic Inspiration
    die, a d6.

    Once within the next 10 minutes, the creature can roll the die and add the
    number rolled to one ability check, attack roll, or saving throw it makes.
    The creature can wait until after it rolls the d20 before deciding to use
    the Bardic Inspiration die, but must decide before the DM says whether the
    roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is
    lost. A creature can have only one Bardic Inspiration die at a time.

    You can use this feature a number of times equal to your Charisma modifier
    (a minimum of once). You regain any expended uses when you finish a long
    rest.

    Your Bardic Inspiration die changes when you reach certain levels in this
    class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at
    15th level.
    """

    if Bard.level >= 2:
        Bard.class_abilities[
            "Jack of All Trades"
        ] = """
        Starting at 2nd level, you can add half your proficiency bonus, rounded
        down, to any ability check you make that doesn’t already include your
        proficiency bonus.
        """
        Bard.class_abilities[
            "Song of Rest"
        ] = """
        Beginning at 2nd level, you can use soothing music or oration to help
        revitalize your wounded allies during a short rest. If you or any
        friendly creatures who can hear your performance regain hit points at
        the end of the short rest by spending one or more Hit Dice, each of
        those creatures regains an extra 1d6 hit points.

        The extra hit points increase when you reach certain levels in this
        class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th
        level.
        """

    if Bard.level >= 3:
        Bard.class_abilities[
            "Expertise"
        ] = """
        At 3rd level, choose two of your skill proficiencies. Your proficiency
        bonus is doubled for any ability check you make that uses either of the
        chosen proficiencies.

        At 10th level, you can choose another two skill proficiencies to gain
        this benefit.
        """
        Bard.subclass = random.choice(list(college))

        if Bard.subclass == college.CollegeOfLore:
            Bard.class_abilities[
                "Bonus Proficiencies"
            ] = """
            When you join the College of Lore at 3rd level, you gain
            proficiency
            with three skills of your choice.
            """
            Bard.class_abilities[
                "Cutting Words"
            ] = """
            Also at 3rd level, you learn how to use your wit to distract,
            confuse, and otherwise sap the confidence and competence of others.
            When a creature that you can see within 60 feet of you makes an
            attack roll, an ability check, or a damage roll, you can use your
            reaction to expend one of your uses of Bardic Inspiration, rolling
            a Bardic Inspiration die and subtracting the number rolled from the
            creature’s roll. You can choose to use this feature after the
            creature makes its roll, but before the DM determines whether the
            attack roll or ability check succeeds or fails, or before the
            creature deals its damage. The creature is immune if it can’t hear
            you or if it’s immune to being charmed.
            """

        if Bard.subclass == college.CollegeOfValor:
            Bard.class_abilities[
                "Bonus Proficiencies"
            ] = """
            When you join the College of Valor at 3rd level, you gain
            proficiency with medium armor, shields, and martial weapons.
            """
            Bard.class_abilities[
                "Combat Inspiration"
            ] = """
            Also at 3rd level, you learn to inspire others in battle. A
            creature that has a Bardic Inspiration die from you can roll that
            die and add the number rolled to a weapon damage roll it just made.
            Alternatively, when an attack roll is made against the creature, it
            can use its reaction to roll the Bardic Inspiration die and add the
            number rolled to its AC against that attack, after seeing the roll
            but before knowing whether it hits or misses.
            """
    return Bard
