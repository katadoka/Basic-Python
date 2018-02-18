# Transposition of the matrix using List comprehension.

a = [[0,1,2,], [2,3,4]]
print([list(i) for i in zip(*a)])
