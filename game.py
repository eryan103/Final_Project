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

# def game():
#     #load player stats and inventory from files
#     load_stats()
#     load_inventory()

#     print("Hello adventurer! It is time to embark on your journey.")
#     print("If you need to check your inventory, type: INV")
#     print("If you need to check your stats, type: STATS")

#     validDirections = ['n','e','w','s']
#     while True:
#         userInput = input("Which direction would you like to travel? (N, S, E, W):\n")
#         userInput = userInput.lower().strip()
#         if userInput not in validDirections:
#             print("Invalid direction. Please choose N, S, E, or W.")
#             continue
#         if (userInput == "N"):
#             print(f{blacksmith})
   
   
 
   #Main game loop
def main():
    while True:
        current_location = field()
        action = input(f"Current Location: {current_location}\n"
                       "Which direction would you like to travel? (N, S, E, W): ").strip().upper()
        
        if action == 'N' or action == 'E' or action == 'S' or action == 'W':

            if action == 'N':
                current_location == blacksmith(player_stats)

            elif action == 'S': #apothecary
                current_location == apothecary(myInventory)

            elif action == 'E': #trainer
                current_location = trainer()

            elif action == 'W': #priest
                current_location = priest()
                continue

        elif action == 'STATS':
            for STATS in player_stats['Stats']:
                print(f"Stats: - {STATS}")
        elif action == 'INV':
            for INV in myInventory['items']:
                print(f"Inventory: - {INV}")
        elif action == 'Q':
            print("Thanks for playing!")
            save_stats()
            save_inventory()
            break

        else:
            print("Invalid direction. Please choose N, S, E, or W.")

    

main()
    