from npc import Npc
from races.dragonborn import Dragonborn
from races.dwarf import Dwarf
from races.elf import Elf
from races.gnome import Gnome
from races.halfelf import HalfElf
from races.halfling import Halfling
from races.halforc import HalfOrc
from races.human import Human
from races.tiefling import Tiefling


def test_create_npc_with_race_specified():
    npc = Npc(race=Human)
    assert npc.race is Human


def test_create_npc_without_race_specified():
    available_races = [
        Dragonborn,
        Dwarf,
        Elf,
        Gnome,
        HalfElf,
        Halfling,
        HalfOrc,
        Human,
        Tiefling,
    ]
    npc = Npc()
    assert npc.race in available_races


def test_create_npc_default_level_is_1():
    npc = Npc()
    assert npc.npc_class.level == 1


def test_create_npc_level_2():
    npc = Npc(level=2)
    assert npc.npc_class.level == 2
