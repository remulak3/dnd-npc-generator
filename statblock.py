from npc import Npc
import json


def convert_npc_to_statblock_json(npc: Npc):
    obj = {
        "name": "NPC",
        "size": str(npc.race.size).lower(),
        "type": "humanoid",
        "tag": "",
        "alignment": "any alignment",
        "hitDice": str(npc.npc_class.hit_dice),
        "armorName": "none",
        "shieldBonus": 0,
        "natArmorBonus": 3,
        "otherArmorDesc": "10",
        "speed": str(npc.race.speed),
        "burrowSpeed": "0",
        "climbSpeed": "0",
        "flySpeed": "0",
        "hover": False,
        "swimSpeed": "0",
        "customHP": False,
        "customSpeed": False,
        "hpText": "22 (5d8)",
        "speedDesc": "30 ft.",
        "strPoints": npc.ability_scores.scores["strength"],
        "dexPoints": npc.ability_scores.scores["dexterity"],
        "conPoints": npc.ability_scores.scores["constitution"],
        "intPoints": npc.ability_scores.scores["intelligence"],
        "wisPoints": npc.ability_scores.scores["wisdom"],
        "chaPoints": npc.ability_scores.scores["charisma"],
        "blindsight": "0",
        "blind": False,
        "darkvision": npc.race.darkvision,
        "tremorsense": "0",
        "truesight": "0",
        "telepathy": 0,
        "cr": npc.npc_class.level,
        "customCr": "1 (200 XP)",
        "customProf": 2,
        "isLegendary": False,
        "legendariesDescription": "The monster can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The monster regains spent legendary actions at the start of its turn.",
        "isLair": False,
        "lairDescription": "When fighting inside its lair, the monster can invoke the ambient magic to take lair actions. On initiative count 20 (losing initiative ties), the monster can take one lair action to cause one of the following effects:",
        "lairDescriptionEnd": "The monster can't repeat an effect until they have all been used, and it can't use the same effect two rounds in a row.",
        "isMythic": False,
        "mythicDescription": "If the monster's mythic trait is active, it can use the options below as legendary actions for 1 hour after using {Some Ability}.",
        "isRegional": False,
        "regionalDescription": "The region containing the monster's lair is warped by the creature's presence, which creates one or more of the following effects:",
        "regionalDescriptionEnd": "If the monster dies, the first two effects fade over the course of 3d10 days.",
        "properties": [],
        "abilities": [
            {
                "name": "Reckless Attack",
                "desc": "Starting at 2nd level, you can throw aside all concern for defense to\n        attack with fierce desperation. When you make your first attack on your\n        turn, you can decide to attack recklessly. Doing so gives you advantage on\n        melee weapon attack rolls using Strength during this turn, but attack\n        rolls against you have advantage until your next turn.",
            },
            {
                "name": "Danger Sense",
                "desc": "At 2nd level, you gain an uncanny sense of when things nearby aren’t as\n        they should be, giving you an edge when you dodge away from danger.\n\n        You have advantage on Dexterity saving throws against effects that you can\n        see, such as traps and spells. To gain this benefit, you can’t be blinded,\n        deafened, or incapacitated.",
            },
        ],
        "actions": [],
        "bonusActions": [],
        "reactions": [],
        "legendaries": [],
        "mythics": [],
        "lairs": [],
        "regionals": [],
        "sthrows": [],
        "skills": [],
        "damagetypes": [],
        "specialdamage": [],
        "conditions": [],
        "languages": [],
        "understandsBut": "",
        "shortName": "",
        "pluralName": "",
        "doubleColumns": True,
        "separationPoint": 0,
        "damage": [],
    }
    for ability in npc.npc_class.class_abilities:
        obj["abilities"].append(
            {"name": ability, "desc": npc.npc_class.class_abilities[ability]}
        )

    json_obj = json.dumps(obj)
    return json_obj
