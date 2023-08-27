def roll_call_dwarves(dwarves):
    i=0
    while i<len(dwarves):
        print(f'{i+1}. {dwarves[i]}')
        i += 1
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
def summon_captain_planet(planeteer_calls):
    return [planet.title()+'!' for planet in planeteer_calls]

def long_planeteer_calls(calls):
    found = False
    for item in calls:
        if(len(item)>4):
            found=True
    return found

def find_the_cheese(snacks):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for snack in snacks:
        if(snack in cheeses):
            return snack

#roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
#long_planeteer_calls(["two", "go", "industrious", "bop"])
#print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))