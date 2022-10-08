def testing(number):
    for i in range(number):
        yield i 

one_test = testing(4)
print(next(one_test))
print(next(one_test))