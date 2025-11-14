def first_ten_digits(num: str) -> int:
    """
    Calculate the first ten digits of the sum of all digits of a given number
    """
    digit_sum = sum(int(d) for d in num)
    return int(str(digit_sum)[:10])
