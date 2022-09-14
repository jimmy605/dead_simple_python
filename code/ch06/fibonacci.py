def fibonacci_next(series=None):
    if series == None:
        series = [1, 1]
    series.append(series[-1] + series[-2])
    return series

