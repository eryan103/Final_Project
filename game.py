'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# main game logic

from locations import blacksmith, apothecary, trainer, priest
from inventory import add_item, show_inventory
from stats import player_stats

def main():
    print("Hello adventurer! It is time to embark on your journey.")
    print("If you need to check your inventory, type: INV")
    print("If you need to check your stats, type: STATS")

    #Main game loop
    while True:
        print("Current Location: The field")
        direction = input("Which direction would you like to travel? (N, S, E, W)")

        if direction == 'N': #blacksmith
            blacksmith()
        elif direction == 'S': #apothecary
            apothecary()
        elif direction == 'E': #trainer
            trainer()
        elif direction == 'W': #priest
            priest()
        else:
            print("Invalid direction. Please choose N, S, E, or W.")
        

    #in case player wants to check stats or inventory
        action = input("Type 'INV' to check inventory or 'STATS' to check stats: ")

        if action == 'INV':
            print((f"Inventory: "))
        elif action == 'STATS':
            print(f"Health: {player_stats.health}/10, Stamina: {player_stats.stamina}/10, Skill: {player_stats.skill}/10")
            break

main()
    