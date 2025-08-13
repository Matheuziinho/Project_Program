# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
# any remainder.
#
# What is the smallest positive number that is evenly divisible by all numbers from 1 to 20?


from functools import reduce


def sequence_numbers(n: int) -> list[int]:
    return list(range(1, n + 1))


def max_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    if num >= 1:
        for i in sequence_numbers(n):
            if num % i == 0:
                i += 1
                factors.append(i)
    return factors


def smallest_multiple(n: int) -> int:
    return reduce(lambda x, y: x * y, set(max_prime_factors(n)))
