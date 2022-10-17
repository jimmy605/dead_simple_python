with open('78SomewhereRd.txt', 'r') as house:
    lines = house.readlines()
    print(lines)
    print()
    for line in lines:
        print(line.strip())