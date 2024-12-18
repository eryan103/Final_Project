#defines locations and events

from inventory import add_item, show_inventory
from stats import player_stats



# these will be read by main file to say what's happening at what location
def field():
    print("You are in the field. Please choose a direction to travel (N, E, S, W):\n")
    action = input("Direction:\n")
    if action == blacksmith(player_stats):
        print(f"{blacksmith}")

def blacksmith(player_stats):  #blacksmith
    print("You are at the Blacksmith.")
    action = input("Choices: obtain a weapon (+3 skill), go back to the field, or go to the apothecary\n")
    if action.lower() == "obtain a weapon":
        player_stats["skill"] += 3
        print("You obtained a weapon. Skill increased by 3.")
    elif action.lower() == "go back to the field":
        print("Going back to the field.")
        return field()
    elif action.lower() == "go to the apothecary":
        print("Going to the apothecary.")
        return apothecary()
    return blacksmith(player_stats)

def apothecary():
    print("You are at the Apothecary.")
    action = input("Choices: Obtain healing herbs (added to inventory, +3 health), go back to the field, or go to the trainer\n:")
    if action.lower() == "obtain healing herbs":
        add_item("Healing Herbs (+3 health)")
        print("You obtained healing herbs. You can use them later.")
    elif action.lower() == "go back to the field":
        print("Going back to the field.")
        return field()
    elif action.lower() == "go to the trainer":
        print("Going to the trainer.")
        return trainer()
    return apothecary()

def trainer():
    print("You are at the Trainer.")
    action = input("Choices: Be trained (+5 skill), go back to the field, or go to the inn\n")
    if action.lower() == "be trained":
        player_stats['skill'] += 5
        print("You received training. Skill increased by 5.")
    elif action.lower() == "go back to the field":
        print("going back to the field.")
        return "field"
    elif action.lower() == "go to the inn":
        print("Going to the inn.")
        return inn()
    return trainer()

def priest():
    print("You are at the Priest.")
    action = input("Choices: Full health/stamina restore, obtain potion, go back to field, go to mountain")
    if action.lower() == "restore":
        player_stats['health'] = 10
        player_stats['stamina'] = 10
    elif action.lower() == "potion":
        add_item("Potion added to inventory, properties are +5 health and +5 stamina")
    elif action.lower() == "field":
        return field()
    elif action.lower() == "mountain":
        return mountain()
    return priest()


def inn():
    print("You are at the Inn.")
    action = input("Choices: Sleep (full health/stamina restore, +1 skill), drinking competition (-5 health, -5 stamina, +2 skill), go back to the field, or go to the mountain:\n")
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
        return field()
    elif action.lower() == "go to the mountain":
        return mountain()
    return inn()
    
def mountain():
    print("You are the Mountain.")
    action = input("Choices: Proceed to Cave or Go back to Field:\n")
    if action.lower() == "proceed to cave":
        return cave()
    elif action.lower() == "go back to field":
        return field()
    
def cave():
    print("You've come across an angry frost troll!"
          "They are coming straight after you. It's time to fight!")
    if player_stats['skill'] >= 9:
        print("You won the game! Congratulations.")
    elif player_stats['skill'] == 8:
        print("You wake up in the field with your head pounding"
              "You wonder if it was all a dream.")
        return field()
    elif player_stats['skill'] < 7:
        print("You lost!")  #figure out way to make them die and go back to field
        #w/o their inventory items and go back to original stats