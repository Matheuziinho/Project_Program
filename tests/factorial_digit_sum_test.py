from project_program.factorial_digit_sum import factorial_digit_sum


def test_factorial_digit_sum_10():
    assert (
        factorial_digit_sum(10) == 27
    )  # 10! = 3628800, sum of digits = 3+6+2+8+8+0+0 = 27
