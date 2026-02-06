# Factorial digit sum

import math


def factorial(num):
    if num <= 0:
        return 1
    else:
        return math.factorial(num)


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def factorial_digit_sum(n):
    fact = factorial(n)
    return sum_of_digits(fact)
