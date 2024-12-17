'''
Emily Ames
COS 121
Final Project
12/17/2024
'''
# main game logic

def main(): #these are the player's beginning stats
    health = 10
    stamina = 10
    skill = 1
    inventory = []

    print("Welcome to the Adventure Game!\n")

    while True:  #shows user what their current stats are
        print(f"Health: {health}/10, Stamina: {stamina}/10, Skill: {skill}/10")

