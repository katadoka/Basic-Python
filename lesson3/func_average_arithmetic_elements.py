# a function that accepts an array
# and returns the arithmetic mean of its elements


def averege_arithmetic(mass):
    aver = sum(mass)/len(mass)
    return aver

mass = [int(x) for x in input("Enter the numbers: ").split()]
print(averege_arithmetic(mass))
