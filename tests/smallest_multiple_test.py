from project_program.smallest_multiple import (
    max_prime_factorials,
    sequence_numbers,
    smallest_multiple,
)


def test_sequence_numbers() -> None:
    assert sequence_numbers(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sequence_numbers(20) == list(range(1, 21))


def test_max_prime_factorials() -> None:
    assert max_prime_factorials(10) == [5, 7]
    assert max_prime_factorials(20) == [5, 7, 11, 13, 17, 19]


def test_smallest_multiple() -> None:
    assert smallest_multiple(10) == 2520
    assert smallest_multiple(20) == 232792560
