# Testing code examples out

# spam = 123456789
# maps = spam

# eggs = 123456789

# print(spam is maps)
# print(spam is eggs)

# def spacing(n):
#     for i in range(n):
#         print()

# for i in [spam, maps, eggs]:
#     print(id(i),end=spacing(4))

def find_lowest(temps):
    sorted_temps = sorted(temps) # sorted returns a new list
    print(sorted_temps[0])

t = [85, 76, 79, 72, 81]
find_lowest(t)
print(t)