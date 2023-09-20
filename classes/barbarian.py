from npc_class import NpcClass
import random
from enum import Enum, auto


class path(Enum):
    PathOfTheBerserker = auto()
    PathOfTheTotemWarrior = auto()


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
        turn, you can decide to attack recklessly. Doing so gives you 
        advantage on melee weapon attack rolls using Strength during this turn,
        but attack rolls against you have advantage until your next turn.
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

    if Barbarian.level >= 3:
        Barbarian.subclass = random.choice(list(path))

        if Barbarian.subclass == path.PathOfTheBerserker:
            Barbarian.class_abilities[
                "Frenzy"
            ] = """
            Starting when you choose this path at 3rd level, you can go into a
            frenzy when you rage. If you do so, for the duration of your rage
            you can make a single melee weapon attack as a bonus action on
            each of your turns after this one. When your rage ends, you suffer
            one level of exhaustion.
            """
        if Barbarian.subclass == path.PathOfTheTotemWarrior:
            Barbarian.class_abilities[
                "Spirit Seeker"
            ] = """
            Yours is a path that seeks attunement with the natural world,
            giving you a kinship with beasts. At 3rd level when you adopt this
            path, you gain the ability to cast the beast sense and speak with
            animals spells, but only as rituals.
            """
            Barbarian.class_abilities[
                "Totem Spirit"
            ] = """
            At 3rd level, when you adopt this path, you choose a totem spirit
            and gain its feature. You must make or acquire a physical totem
            object — an amulet or similar adornment — that incorporates fur or
            feathers, claws, teeth, or bones of the totem animal. At your
            option, you also gain minor physical attributes that are
            reminiscent of your totem spirit. For example, if you have a bear
            totem spirit, you might be unusually hairy and thick-skinned, or
            if your totem is the eagle, your eyes turn bright yellow.

            Your totem animal might be an animal related to those listed here
            but more appropriate to your homeland. For example, you could
            choose a hawk or vulture in place of an eagle.

            - Bear. While raging, you have resistance to all damage except
            psychic damage. The spirit of the bear makes you tough enough to
            stand up to any punishment.

            - Eagle. While you’re raging, other creatures have disadvantage on
            opportunity attack rolls against you, and you can use the Dash
            action as a bonus action on your turn. The spirit of the eagle
            makes you into a predator who can weave through the fray with ease.

            - Wolf. While you’re raging, your friends have advantage on melee
            attack rolls against any creature within 5 feet of you that is
            hostile to you. The spirit of the wolf makes you a leader of
            hunters.
            """
    return Barbarian
