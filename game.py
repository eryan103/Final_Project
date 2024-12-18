'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# this is where the main game loop takes place.

from locations import *   #imports everything from locations file
from stats import *    #imports everything from stats file

   
   
 
   
def main():
    print("Hello adventurer! It is time to embark on your journey.")
    userInput = input("Please enter your character's name:\n")   #will be stored for later
    f = open("field.txt","r")  #this is opening up the text description about the field
    print(f.read()) # this prints what is written on the field.txt file
    f.close()  #lets the code move on
    player_stats['name'] = userInput
    world = {}    #empty dictionary so we can add different locations
    world['loc'] = 'field'   #we always start in the field. the user can choose directions from here
    while True:
        if world['loc'] == "field":
            field(world)
        if world ['loc'] == "blacksmith":
            blacksmith(player_stats, world)
        if world ['loc'] == "apothecary":
            apothecary(world)
        if world ['loc'] == "trainer":
            trainer(player_stats, world)
        if world['loc'] == "inn":
            inn(player_stats, world)
        if world ['loc'] == "priest":
            priest(player_stats, world)
        if world ['loc'] == "mountain":
            mountain(world)
        if world ['loc'] == "cave":
            cave(player_stats, save_stats, world)

main()
    