# Write in the last element of the matrix line the sum of all the previous line items using List comprehension 
# and functional programming.
from functools import reduce

a = ([0,1,2,4,3,2])

a1 = a[:-1]
a1.append(reduce(lambda x, y: x + y,a))
print(a1)
