# the user enters a number, the sequence of numbers is changed to the opposite


def reverse_number(number):
    reverse = 0
    while(number > 0):
        number1 = number % 10
        reverse = (reverse * 10) + number1
        number = number // 10
    return reverse

number = int(input('Enter the number: '))
print('Reverse the number: ', reverse_number(number))
