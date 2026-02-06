from project_program.amicable_numbers import counting_amicable_pairs


def test_counting_amicable_pairs() -> None:
    assert counting_amicable_pairs(1000) == 1  # (220, 284)
