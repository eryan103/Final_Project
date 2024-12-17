# keeps track of player stats

player_stats = {
    'health': 10,
    'stamina': 10,
    'skill': 1
}

def show_stats():
    print(f"Health: {player_stats['health']}/10")
    print(f"Stamina: {player_stats['stamina']}/10")
    print(f"Skill: {player_stats['skill']}/10")
