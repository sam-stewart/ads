#!/usr/bin/python


def fizzbuzz(x):
    """ Return Fizz if x is multiple of 3, Buzz if multiple of 5, FizzBuzz if
    multiple of three and five. Maximum two comparisons. There are less
    multiples of 5 than 3, so testing for three nested in 5 makes sense. """
    if x % 5 == 0:
        if x % 3 == 0:
            return 'FizzBuzz'
        return 'Buzz'
    if x % 3 == 0:
        return 'Fizz'
    return str(x)

if __name__ == '__main__':
    for x in range(1, 101):
        print fizzbuzz(x)
