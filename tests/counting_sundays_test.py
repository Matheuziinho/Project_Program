from project_program.counting_sundays import counting


def test_counting():
    assert counting(1901, 2000) == 5218
