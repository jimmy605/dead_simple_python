class AverageCalculator:
    
    def __init__(self):
        self.total = 0
        self.count = 0
    
    def __call__(self, *values):
        if values: 
            for value in values:
                self.total += float(value)
                self.count += 1
            return self.total/self.count 

average = AverageCalculator()
values = input('Enter scores, seperated by spaces:\n    ').split()
try:
    print(f'Average is {average(*values)}')
except ZeroDivisionError:
    print('ERROR: No values provided.')
except (ValueError, UnicodeError):
    print(f'ERROR: All inputs should be numeric.')
