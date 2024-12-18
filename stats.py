# keeps track of player stats

player_stats = {
    "Stats"
    'health': 10,
    'stamina': 10,
    'skill': 1
}


#loading stats from a file
def load_stats():
    try:
        with open('player_stats.txt', 'r') as file:
            stats = file.read().splitlines()
            player_stats['health'] = int(stats[0])
            player_stats['stamina'] = int(stats[1])
            player_stats['skill'] = int(stats[2])
    except FileNotFoundError:
        print("No saved stats found, using default stats.")
    return player_stats

#save stats to a file
def save_stats():
    with open('player_stats.txt', 'w') as file:
        file.write(f"{player_stats['health']}\n")
        file.write(f"{player_stats['stamina']}\n")
        file.write(f"{player_stats['skill']}\n")

def show_stats():
    print(f"Health: {player_stats['health']}/10")
    print(f"Stamina: {player_stats['stamina']}/10")
    print(f"Skill: {player_stats['skill']}/10")