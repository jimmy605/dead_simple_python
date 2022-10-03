menu = {'drip': 1.95, 'capuccino': 2.95, 'americano': 2.49}

def checkout(order):
    if order in menu:
        print(f'Your total is {menu[order]}')
    else:
        print('That item is not on the menu.')


checkout('drip')
checkout('tea')