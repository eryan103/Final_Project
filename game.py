'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# main game logic

from locations import handle_location_event
from inventory import Inventory
from stats import Stats

def main(): #these are the player's beginning stats
    player_stats = Stats(health = 10, stamina = 10, skill = 1)
    player_inventory = Inventory()

    print("Hello adventurer! It is time to embark on your journey.")
    print("If you need to check your inventory, type: INV")
    print("If you need to check your stats, type: STATS")

    #Main game loop
    while True:
        print("Current Location: The field")
        direction = input("Which direction would you like to travel? (N, S, E, W)")

        if direction in ['N', 'S', 'E', 'W']:
           player_stats, player_inventory = handle_location_event(direction, player_stats, player_inventory)  
        else:
             print("Invalid direction. Please choose N, S, E, or W.")
    