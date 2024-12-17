#defines locations and events

from inventory import Inventory
from stats import Stats

# these will be read by main file to say what's happening at what location
def handle_location_event(direction, player_stats, player_inventory):
    if direction == 'N':  #blacksmith
        print("You are at the Blacksmith.")
        action = input("Choices: obtain a weapon (+3 skill), go back to the field, or go to the apothecary\n")
        if action.lower() == "obtain a weapon":
            player_stats.skill += 3
            print("You obtained a weapon. Skill increased by 3.")
        elif action.lower() == "go back to the field":
            print("Going back to the field.")
        elif action.lower() == "go to the apothecary":
            return handle_location_event(player_stats, player_inventory)