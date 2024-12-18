# keeps track of player stats

player_stats = {
    'health': 10,
    'stamina': 10,
    'skill': 1,
    'name':' ',
    'outcome': ' '
    }


#save stats to a file
def save_stats():
    f = open("data.txt", "w")
    (f.write(f"Name:{player_stats['name']}\n",))
    (f.write(f"Outcome:{player_stats['outcome']}\n"))
    (f.write(f"Hp:{player_stats['health']}\n"))
    (f.write(f"Stamina:{player_stats['stamina']}\n"))
    (f.write(f"Skill:{player_stats['skill']}\n"))
    f.close()

def show_stats():
    print(f"Health: {player_stats['health']}/10")
    print(f"Stamina: {player_stats['stamina']}/10")
    print(f"Skill: {player_stats['skill']}/10")