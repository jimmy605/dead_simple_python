from collections import deque

customers = deque(['kyle', 'Simon', 'James', 'Daniel'])
# first, second, third = customers 
# print(second)

first, *middle, last = customers
print(first)
print(middle)
print(last)

