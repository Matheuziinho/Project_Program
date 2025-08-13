# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two digit numbers is 9009 = 91*99.
# Find the largest palindrome made from the product of two digit numbers.


def string_inverse(n: int) -> str:
    return str(n)[::-1]


def max_palindrome(digit_number: int) -> int:
    interval = range(10 ** (digit_number), 10 ** (digit_number - 1), -1)
    max_pal = 0
    num1 = 0
    num2 = 0
    for num1 in interval:
        for num2 in interval:
            product = num1 * num2
            if str(product) == string_inverse(product):
                num1 += 1
                num2 += 1
                max_pal = max(max_pal, product)
    return max_pal
