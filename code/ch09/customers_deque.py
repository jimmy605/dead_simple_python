from collections import deque

customers = deque(['Daniel', 'Denis'])
customers.append('Simon')
print(customers)

customer = customers.popleft()
print(customer)
print(customers)

customers.appendleft('James')
print(customers)

last_in_line = customers.pop()
print(last_in_line)
