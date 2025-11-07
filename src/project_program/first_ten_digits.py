def first_ten_digits(num):
    """
    Calculate the first ten digits of the sum of all digits of a given number
    """
    digit_sum = sum(int(d) for d in str(abs(num)))
    return int(str(digit_sum)[:10])
