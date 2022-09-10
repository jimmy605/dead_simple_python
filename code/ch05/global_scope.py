high_score = 10

def score():
    global high_score
    new_score = 465
    if new_score > high_score:
        print('New high score')
        high_score = new_score

score()
print(high_score)