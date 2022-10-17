# with open('78SomewhereRd.txt', 'r') as house:
#     for line in house:
#         print(line.strip())


# with open('78SomewhereRd.txt', 'r') as house:
#     for _ in range(3):
#         print(house.readline().strip())
#         house.seek(0)


with open('78SomewhereRd.txt', 'r') as house:
    for n in range(10):
        house.seek(n)
        print(house.readline().strip())