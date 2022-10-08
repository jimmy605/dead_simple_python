
orders = ['cold brew', 'lemongrass tea', 'chai latte', 'medium drip','french press', 'mocha cappuccino', 'pumpkin spice latte',
'double-shot espresso', 'dark roast drip','americano']

drip_orders = [order for order in orders if 'drip' in order]
print(f'There are {len(drip_orders)} orders for drip coffee.')

name = 'Dean ONeill'
name_list = ([char for char in name])

for i in name_list:
    print(i)

