# keeps track of player stats

player_stats = {    #dictionary #initial stats 
    'health': 10,
    'stamina': 10,
    'skill': 1,
    'name':' ',
    'outcome': ' '    #keep open apostrophe to add content later
    }


#save stats to a file
def save_stats():
    f = open("data.txt", "w")   #opens file to write to it
    (f.write(f"Name:{player_stats['name']}\n",))    #label stats from dictionary so user can see what they represent
    (f.write(f"Outcome:{player_stats['outcome']}\n"))
    (f.write(f"Hp:{player_stats['health']}\n"))
    (f.write(f"Stamina:{player_stats['stamina']}\n"))
    (f.write(f"Skill:{player_stats['skill']}\n"))
    f.close()   #closes file

def show_stats():  #can be utilized to show the stats to the user in an aesthetically pleasing way
    print(f"Health: {player_stats['health']}/10")
    print(f"Stamina: {player_stats['stamina']}/10")
    print(f"Skill: {player_stats['skill']}/10")

# if player_stats['health'] == 0:
#     print("You lost. You didn't even fight anything.")
# if player_stats['stamina'] == 0:
#     print("You are exhausted.")