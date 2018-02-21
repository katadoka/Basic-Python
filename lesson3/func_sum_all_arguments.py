# the function will return the sum of all arguments.


def sum_args(*args):
    return sum(int(i) for i in args)

assert sum_args(1) == 1
assert sum_args(1, 2, 3, 4) == 10
assert sum_args(10, 15) == 25
