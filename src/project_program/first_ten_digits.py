def first_ten_digits(num):
    """
    Calculate the first ten digits of the sum of all digits of a given number
    """

    num_str = str(num)

    digit_sum = 0
    for digit_char in num_str:
        digit_sum += int(digit_char)

    return int(str(digit_sum)[:10])
