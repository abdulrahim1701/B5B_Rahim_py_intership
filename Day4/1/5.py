from functools import reduce

numbers = [12, 45, 7, 89, 23, 56]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print(largest)