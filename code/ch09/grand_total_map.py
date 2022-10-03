cost = [5.95, 4.95, 5.45, 3.45, 2.95]
tip = [0.25, 1.00, 2.00, 0.15, 0.00]

def total(c, t):
    return c + t

for total_expense in map(total, cost, tip):
    print(f'{total_expense:.2f}')
