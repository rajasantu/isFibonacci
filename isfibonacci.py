import math


def square(x):    # to check if x is perfect square
    s = int(math.sqrt(x))
    return s*s == x


def fibonacci(n):   # returns true if n is a fibonacci number
    # n is fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return square(5*n*n + 4) or square(5*n*n - 4)


def is_fibonacci(lst):   # function to check if each number of list is fibonacci or not

    for i in lst:
        if fibonacci(i) is True:
            print(i, 'is a fibonacci')
        else:
            print(i, 'is not a fibonacci')


list1 = [1, 3, 6, 4, 9, 15, 9, 13]
is_fibonacci(list1)
