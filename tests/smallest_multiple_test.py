from project_program.smallest_multiple import max_prime_factors, smallest_multiple


def test_max_prime_factors() -> None:
    assert max_prime_factors(20) == [2, 5, 7, 11, 13, 17, 19]


def test_smallest_multiple() -> None:
    assert smallest_multiple(10) == 2520
    assert smallest_multiple(20) == 232792560
