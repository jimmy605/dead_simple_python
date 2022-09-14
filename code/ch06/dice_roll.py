import random 

def roll_dice(sides):
    return random.randint(1, sides)

print('Roll for initiative...')
player1 = roll_dice(20)
player2 = roll_dice(20)

for _ in range(10):
    player1 = roll_dice(20)
    player2 = roll_dice(20)
    
    if player1 >= player2:
        print(f'Player 1 goes first (rolled {player1})')
    else:
        print(f'Player 2 goes first (rolled {player2})')
    print()


def roll_dices(sides, dice):
    return (random.randint(1, sides) for _ in range(dice))

test = roll_dices(20, 11)

for check in test:
    print(check)