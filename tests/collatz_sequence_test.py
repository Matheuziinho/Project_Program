from project_program.collatz_sequence import biggest_sequence, collatz


def test_biggest_collatz():
    print(biggest_sequence(1_000_000))
    assert biggest_sequence(1_000_000) == 525
