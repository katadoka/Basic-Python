# Find the sum of all positive numbers that have 2 digits.

a = [2, 3, 89, 54, 321, 321, 43, 12]

print(sum(list(filter(lambda x: x > 9 and x < 100, a))))
