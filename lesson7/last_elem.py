# # Write in the last element of the matrix line the sum of
# all the previous line items using List comprehension
# and functional programming.

a = [[1, 2, 3, 4], [2, 3, 5, 6, 7]]
print([row[:-1] + [sum(row)] for row in a])
