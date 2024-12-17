'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# main game logic

from locations import blacksmith, apothecary, trainer
from inventory import inventory, load_inventory, save_inventory, show_inventory
from stats import player_stats, load_stats, save_stats, show_stats

def main():
    #load player stats and inventory from files
    load_stats()
    load_inventory()

    current_location = "field"

    print("Hello adventurer! It is time to embark on your journey.")
    print("If you need to check your inventory, type: INV")
    print("If you need to check your stats, type: STATS")

    #Main game loop
    while True:
        action = input(f"Current Location: {current_location.capitalize()}\n"
                       "Which direction would you like to travel? (N, S, E, W): ").strip().upper()
        
        if action == 'N' or action == 'E' or action == 'S' or action == 'W':
            if action == 'N':
                current_location = 'blacksmith'
                blacksmith(player_stats)
            elif action == 'S': #apothecary
                current_location = 'apothecary'
                apothecary()
            elif action == 'E': #trainer
                current_location = 'trainer'
                trainer()
        #   elif action == 'W': #priest
        #       current_location = 'priest'
                #priest()
        elif action == 'STATS':
            show_stats()
        elif action == 'INV':
            print(f"Inventory: {show_inventory()}")
        elif action == 'Q':
            print("Thanks for playing!")
            save_stats()
            save_inventory()
            break
        
        else:
            print("Invalid direction. Please choose N, S, E, or W.")

        

    # #in case player wants to check stats or inventory
    #     action = input("Type 'INV' to check inventory or 'STATS' to check stats, or 'Q' to quit the game: ").strip().upper()
    #     if action == 'INV':
    #         print((f"Inventory: {show_inventory()} "))
    #     elif action == 'STATS':
    #         show_stats()
    #     elif action == 'Q':
    #         print("Thanks for playing!")
    #         save_stats()   #save player stats
    #         save_inventory()  #save inventory
    #         break 

main()
    