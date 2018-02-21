# the function that returns the factorial of the number.


def factor(number):
    if number == 1:
        return number
    else:
        return number*factor(number - 1)

number = int(input('Enter the number: '))
print(factor(number))
