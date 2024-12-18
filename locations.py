#defines locations and events

from stats import *   #imports everything from stats file

RESET = "\033[0;0m"
BOLD    = "\033[;1m"  #bold words to show user what to type, this should reduce any user error

# these will be read by main file to say what's happening at what location
def field(world):
    print("Please choose a direction to travel (N, E, S, W):")
    action = input("Direction:\n").strip().upper()    # use strip and upper to cut down user error
    if action == "N":
        world['loc'] = "blacksmith"   #resets world location which will be read by main file game.py
    if action == "S":
        world['loc'] = "apothecary"
    if action == "E":
        world['loc'] = "trainer"
    if action == "W":
        world['loc'] = "priest"
    elif action == "STATS":   #gives the user an opportunity to check their stats from the stats file
        show_stats()



def blacksmith(player_stats, world):  
    print("You are at the Blacksmith.") 
    action = input(f"Choices: obtain a {BOLD}weapon{RESET} (+3 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}apothecary{RESET}\n")
    if action.lower() == "weapon":
        player_stats["skill"] += 3   #adds to skill level in the player stats dictionary
        print("You obtained a weapon. Skill increased by 3.")
    elif action.lower() == "field":
        print("Going back to the field.")
        world['loc'] = "field"   #travels to field
        return
    elif action.lower() == "apothecary":
        print("Going to the apothecary.")
        world['loc'] = "apothecary"   #travels to apothecary
        return
    return

def apothecary(world):
    print("You are at the Apothecary.") 
    action = input(f"Choices: Practice making {BOLD}potions{RESET} (+2 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}trainer{RESET}\n:")
    if action.lower() == "potions":  
        player_stats['skill'] += 2    #gains 2 skill
        print("You practiced making potions. Your skill level has grown.")
    elif action.lower() == "field":  
        print("Going back to the field.")
        world['loc'] = "field"   #travels back to field
        return
    elif action.lower() == "trainer":
        print("Going to the trainer.")
        world['loc'] = "trainer"  #travels to trainer
        return
    return

def trainer(player_stats, world):
    print("You are at the Trainer.")  
    action = input(f"Choices: Be {BOLD}train{RESET}ed (+2 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}inn{RESET}\n")
    if action.lower() == "train":  
        player_stats['skill'] += 2   #increase skill level by 2
        print("You received training. Skill increased by 2.")
    elif action.lower() == "field":  
        world['loc'] = "field"  #return to field
        return
    elif action.lower() == "inn":  
        print("Going to the inn.")
        world['loc'] = "inn"  #travel to inn
        return
    return

def priest(player_stats, world):
    print("You are at the Priest.")  
    action = input(f"Choices: Full health/stamina {BOLD}restore{RESET}, go back to {BOLD}field{RESET}, or go to {BOLD}mountain{RESET}\n")
    if action.lower() == "restore":
        player_stats['health'] = 10   #resets back to 10
        player_stats['stamina'] = 10  #resets back to 10
    elif action.lower() == "field":
        world['loc'] = "field"  #travel to field
        return
    elif action.lower() == "mountain":
        world['loc'] = "mountain"   #travel to mountain
        return
    return


def inn(player_stats, world):
    print("You are at the Inn.") 
    action = input(f"Choices: {BOLD}Sleep{RESET} (full health/stamina restore, +1 skill), {BOLD}drink{RESET}ing competition (-5 health, -5 stamina, +2 skill), go back to the {BOLD}field{RESET}, or go to the {BOLD}mountain{RESET}:\n")
    if action.lower() == "sleep":   #can sleep to fill needs and gain a skill level
        player_stats['health'] = 10   #fills health
        player_stats['stamina'] = 10   #fills stamina
        player_stats['skill'] += 1     # add 1 skill
        print("You rested at the Inn. Health and Stamina restored, +1 skill.")
    elif action.lower() == "drink":  #this option drains user of 5 health and stamina, but increases their skill level
        player_stats['health'] -= 5    #lose 5 health
        player_stats['stamina'] -= 5    #lose 5 stamina
        player_stats['skill'] += 2    #gain 2 skill
        print("You participated in the drinking competition. -5 health, -5 stamina, +2 skill.")
    elif action.lower() == "field":   
        print("Going back to the field.")
        world['loc'] = "field"  #returns user to the field
        return
    elif action.lower() == "mountain":  
        world['loc'] = "mountain"  #travel to mountain
        return
    return
    
def mountain(world):
    print("You are on the Mountain.")
    f = open("warning.txt", "r")   #opens a file containing a warning
    print(f.read())      #prints files contents to terminal
    f.close()      #closes file and moves on
    action = input(f"Choices: Proceed to {BOLD}cave{RESET} or go back to the {BOLD}field{RESET}:\n")
    if action.lower() == "cave":
        world['loc'] = "cave"  #travel to cave
        return
    elif action.lower() == "field":
        world['loc'] = "field"    #return to field
        return
    
def cave(player_stats, save_stats, world):
    print("You've come across an angry frost troll! They are coming straight after you. It's time to fight!")  #boss
    if player_stats['skill'] >= 9:    #players skill must be higher than 9
        print("You won the game! Congratulations.")
        player_stats['outcome'] = "Victory"   #adds victory to player stats
        save_stats()    #writes current stats to the data.txt file
        exit(1)    #ends game
    elif player_stats['skill'] == 8:   #if players skill is equal to 8
        print("You wake up in the field with your head pounding. You wonder if it was all a dream.")
        world['loc'] = "field"   #start over in field
        return
    elif player_stats['skill'] < 7:    #if players skill is less than 7
        player_stats['outcome'] = "Lose"  #updates outcome in player_stats dictionary
        save_stats()   # writes current stats to the data.txt file
        print("You lost!")
        exit(1)  #ends game

