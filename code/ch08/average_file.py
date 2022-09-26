def average_file(path):
    file = open(path, 'r')
    
    try:
        numbers = [float(n) for n in file.readlines()]
    except ValueError as e:
        raise ValueError("file contains non-numeric values.") from e 
    else:
        try:
            return sum(numbers) / len(numbers)
        except ZeroDivisionError as e:
            raise ValueError("Empty file.") from e 
    finally:
        print('Closing file.')
        file.close()

print(average_file('numbers_good.txt'))