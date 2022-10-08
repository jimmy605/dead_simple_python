divis_by_three = (n if n % 3 == 0 else 'Redacted' for n in range(100))

for num in divis_by_three:
    print(num)