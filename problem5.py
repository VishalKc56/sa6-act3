numbers = [1, 2, 3, 4]

n = 3  # to raise each number in the list to the power of n

powered_numbers = list(map(lambda x: x**n, numbers))

# Test the function
print(powered_numbers)