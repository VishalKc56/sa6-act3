strings = ["apple", "banana", "cherry", "date"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

# Test the function
print(sorted_strings)