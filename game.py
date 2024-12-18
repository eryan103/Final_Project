'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# main game logic

from locations import blacksmith, apothecary, trainer, field, priest, mountain, cave
from inventory import myInventory, save_inventory
from stats import player_stats, save_stats

   
   
 
   #Main game loop
def main():
    print("Hello adventurer! It is time to embark on your journey.")
    userInput = input("Please enter your character's name:\n")
    f = open("field.txt","r")
    print(f.read())
    f.close()
    player_stats['name'] = userInput
    world = {}
    world['loc'] = 'field'
    while True:
        if world['loc'] == "field":
            field(world)
        if world ['loc'] == "blacksmith":
            blacksmith(player_stats, world)
        if world ['loc'] == "apothecary":
            apothecary(myInventory, world)
        if world ['loc'] == "trainer":
            trainer(player_stats, world)
        if world ['loc'] == "priest":
            priest(player_stats, myInventory, world)
        if world ['loc'] == "mountain":
            mountain(world)
        if world ['loc'] == "cave":
            cave(player_stats, save_stats)
        

main()
    