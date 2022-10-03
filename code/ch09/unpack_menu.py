menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

# a, b, c = menu.items()
# print(a)
# print(b)
# print(c)

(a_name, a_price), (b_name, b_price), *_ = menu.items()

print(b_price)