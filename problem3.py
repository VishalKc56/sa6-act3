from functools import reduce

numbers = [1, 3, 5, 0, 9, 8]

find_max = lambda numbers: reduce(lambda a, b: a if a > b else b, numbers)



# Test the function
print(find_max(numbers)) 