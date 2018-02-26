# Write program that can be run: 'python main.py -n 10'
# program to use the Click library, in order to get string arguments.
# The program takes a number, generates a list of random numbers
# (the number of numbers is passed through the -n parameter in terminal)
# displays the list itself, then sorted by recession and then its amount.


import click
import random
import numpy as np
import numpy.random as rand


@click.command()
@click.option('--number', '-n', default=1)
def click_massive(number):
    massive = np.random.randint(0, number, 100)
    print(massive)
    print(np.sort(massive)[::-1])
    print(np.sum(massive))

if __name__ == '__main__':
    click_massive()
