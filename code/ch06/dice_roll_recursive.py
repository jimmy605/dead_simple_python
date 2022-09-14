import random 

def roll_dice(sides=6, dice=1):
    def roll():
        return random.randint(1, sides)
    
    if dice < 1:
        return ()
    return (roll(), ) + roll_dice(sides, dice-1)