num_for_user = input('Enter a number: ')

try:
    num = int(num_for_user)
except ValueError:
    print('You didnt enter a valid number.')
    num = 0

print(f'Your number sqaured is {num ** 2}')