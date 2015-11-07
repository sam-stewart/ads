#!/usr/bin/python


def fizzbuzz(x):
    """ Return Fizz if x is multiple of 3, Buzz if multiple of 5, FizzBuzz if
    multiple of three and five. Maximum three comparisons"""
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        if x % 3 == 0:
            return 'FizzBuzz'
        return 'Buzz'
    return str(x)

if __name__ == '__main__':
    for x in range(1, 101):
        print fizzbuzz(x)
