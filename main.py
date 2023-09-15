from npc import Npc
from races.dwarf import Dwarf
mariusz = Npc()
mariusz.race = Dwarf

mariusz.race.describe_race(mariusz.race)
