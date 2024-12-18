#defines locations and events

from inventory import add_item, myInventory, show_inventory
from stats import player_stats

RESET = "\033[0;0m"
BOLD    = "\033[;1m"

# these will be read by main file to say what's happening at what location
def field():
    print("You are in the field. Please choose a direction to travel (N, E, S, W):")
    action = input("Direction:\n")
    if action == "N":
        blacksmith(player_stats)
    elif action == "S":
        apothecary(myInventory)
    elif action == "E":
        trainer(player_stats)
    elif action == "W":
        priest(player_stats, myInventory)
    elif action == "STATS":
        print(player_stats)
    elif action == "INV":
        print(myInventory)


def blacksmith(player_stats):  #blacksmith
    print("You are at the Blacksmith.")
    action = input(f"Choices: obtain a {BOLD}weapon{RESET} (+3 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}apothecary{RESET}\n")
    if action.lower() == "weapon":
        player_stats["skill"] += 3
        print("You obtained a weapon. Skill increased by 3.")
    elif action.lower() == "field":
        print("Going back to the field.")
        return field()
    elif action.lower() == "apothecary":
        print("Going to the apothecary.")
        return apothecary(myInventory)
    return blacksmith(player_stats)

def apothecary(myInventory):
    print("You are at the Apothecary.")
    action = input(f"Choices: Obtain healing {BOLD}herbs{RESET} (added to inventory, +3 health), go back to the {BOLD}field{RESET}, or go to the {BOLD}trainer{RESET}\n:")
    if action.lower() == "herbs":
        myInventory['items'] += "healing herbs +3 health"
        print("You obtained healing herbs. You can use them later.")
    elif action.lower() == "field":
        print("Going back to the field.")
        return field()
    elif action.lower() == "trainer":
        print("Going to the trainer.")
        return trainer(player_stats)
    return apothecary(myInventory)

def trainer(player_stats):
    print("You are at the Trainer.")
    action = input(f"Choices: Be {BOLD}train{RESET}ed (+5 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}inn{RESET}\n")
    if action.lower() == "train":
        player_stats['skill'] += 5
        print("You received training. Skill increased by 5.")
    elif action.lower() == "field":
        print("field.")
        return "field"
    elif action.lower() == "inn":
        print("Going to the inn.")
        return inn(player_stats, myInventory)
    return trainer(player_stats)

def priest(player_stats, myInventory):
    print("You are at the Priest.")
    action = input(f"Choices: Full health/stamina {BOLD} restore{RESET}, obtain {BOLD}potion{RESET}, go back to {BOLD}field{RESET}, go to {BOLD}mountain{RESET}\n")
    if action.lower() == "restore":
        player_stats['health'] = 10
        player_stats['stamina'] = 10
    elif action.lower() == "potion":
        myInventory['items'] += "potion: +5 health and +5 stamina"
        print("Potion added to inventory, properties are +5 health and +5 stamina")
    elif action.lower() == "field":
        return field()
    elif action.lower() == "mountain":
        return mountain()
    return priest(player_stats, myInventory)


def inn(player_stats, myInventory):
    print("You are at the Inn.")
    action = input(f"Choices: {BOLD}Sleep{RESET} (full health/stamina restore, +1 skill), {BOLD}drink{RESET}ing competition (-5 health, -5 stamina, +2 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}mountain{RESET}:\n")
    if action.lower() == "sleep":
        player_stats['health'] = 10
        player_stats['stamina'] = 10
        player_stats['skill'] += 1
        print("You rested at the Inn. Health and Stamina restored, +1 skill.")
    elif action.lower() == "drink":
        player_stats['health'] -= 5
        player_stats['stamina'] -= 5
        player_stats['skill'] += 2
        print("You participated in the drinking competition. -5 health, -5 stamina, +2 skill.")
    elif action.lower() == "field":
        print("Going back to the field.")
        return field()
    elif action.lower() == "mountain":
        return mountain()
    return inn(player_stats, myInventory)
    
def mountain():
    print("You are on the Mountain.")
    action = input(f"Choices: Proceed to {BOLD}cave{RESET} or go back to the {BOLD}field{RESET}:\n")
    if action.lower() == "cave":
        return cave(player_stats)
    elif action.lower() == "field":
        return field()
    
def cave(player_stats):
    print("You've come across an angry frost troll!"
          "They are coming straight after you. It's time to fight!")
    if player_stats['skill'] >= 9:
        print("You won the game! Congratulations.")
        player_stats['outcome'] == "Victory"
        f = open("data.txt","a")
        f.write(f"{player_stats['outcome']}")
        exit(1)
    elif player_stats['skill'] == 8:
        print("You wake up in the field with your head pounding"
              "You wonder if it was all a dream.")
        return field()
    elif player_stats['skill'] < 7:
        player_stats['outcome'] == "Lost"
        f = open("data.txt","a")
        f.write(f"{player_stats['outcome']}")
        print("You lost!")
        exit(1)

