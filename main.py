from npc import Npc
from statblock import convert_npc_to_statblock_json

mariusz = Npc(level=3)
# mariusz.print_npc_info()

with open("statblock.monster", "w") as outfile:
    outfile.write(convert_npc_to_statblock_json(mariusz))
