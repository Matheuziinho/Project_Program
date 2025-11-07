# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
# any remainder.
#
# What is the smallest positive number that is evenly divisible by all numbers from 1 to 20?


from functools import reduce

# from project_program import prime_factors


def max_prime_factors(n: int) -> int:
    factors: list[int] = []
    if n >= 1:
        for i in range(1, n + 1):
            if not n % i:
                #               if prime_factors(i):
                factors.append(i)
    return max(factors)


def smallest_multiple(n: int) -> int:
    return reduce(lambda x, y: x * y, set(max_prime_factors(n)))
