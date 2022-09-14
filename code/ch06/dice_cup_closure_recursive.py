import random

def make_dice_cup(sides=6, dice=1):
    def roll(dice=dice):
        if dice < 1:
            reutrn ()
        die = random.randint(1, sides)
        return (die, ) + roll(dice - 1)
    
    return roll

