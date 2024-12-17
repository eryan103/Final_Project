#defines locations and events

from inventory import add_item, show_inventory
from stats import player_stats



# these will be read by main file to say what's happening at what location


def blacksmith(player_stats):  #blacksmith
        print("You are at the Blacksmith.")
        action = input("Choices: obtain a weapon (+3 skill), go back to the field, or go to the apothecary\n")
        if action.lower() == "obtain a weapon":
            player_stats["skill"] += 3
            print("You obtained a weapon. Skill increased by 3.")
        elif action.lower() == "go back to the field":
            print("Going back to the field.")
            #field()
        elif action.lower() == "go to the apothecary":
            apothecary()

def apothecary():
    print("You are at the Apothecary.")
    action = input("Choices: Obtain healing herbs (added to inventory, +3 health), go back to the field, or go to the trainer\n:")
    if action.lower() == "obtain healing herbs":
        add_item("Healing Herbs (+3 health)")
        print("You obtained healing herbs. You can use them later.")
    elif action.lower() == "go back to the field":
        print("Going back to the field.")
        #field()
    elif action.lower() == "go to the trainer":
        trainer()

def trainer():
    print("You are at the Trainer.")
    action = input("Chioces: Be trained (+5 skill), go back to the field, or go to the inn\n")
    if action.lower() == "be trained":
        player_stats['skill'] += 5
        print("You received training. Skill increased by 5.")
    elif action.lower() == "go back to the field":
        print("going back to the field.")
        #field()
    elif action.lower() == "go to the inn":
        inn()

def inn():
    print("You are at the Inn.")
    action = input("Choices: Sleep (full health/stamina restore, +1 skill), drinking competition (-5 health, -5 stamina, +2 skill), go back to the field, or go to the mountain")
    if action.lower() == "sleep":
        player_stats['health'] = 10
        player_stats['stamina'] = 10
        player_stats['skill'] += 1
        print("You rested at the Inn. Health and Stamina restored, +1 skill.")
    elif action.lower() == "drinking competition":
        player_stats['health'] -= 5
        player_stats['stamina'] -= 5
        player_stats['skill'] += 2
        print("You participated in the drinking competition. -5 health, -5 stamina, +2 skill.")
    elif action.lower() == "go back to the field":
        print("Going back to the field.")
        #field()
    #elif action.lower() == "go to the mountain":
        #mountain()