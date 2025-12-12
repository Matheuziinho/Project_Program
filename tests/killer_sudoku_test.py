from project_program.killer_sudoku import combinations


def test_killer_sudoku() -> None:

    assert list(combinations(1, 1, [])) == [(1,)]
    assert list(combinations(2, 1, [])) == [(2,)]
    assert list(combinations(3, 1, [])) == [(3,)]
    assert list(combinations(4, 1, [])) == [(4,)]
    assert list(combinations(5, 1, [])) == [(5,)]
    assert list(combinations(6, 1, [])) == [(6,)]
    assert list(combinations(7, 1, [])) == [(7,)]
    assert list(combinations(8, 1, [])) == [(8,)]
    assert list(combinations(9, 1, [])) == [(9,)]
    assert list(combinations(45, 9, [])) == [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
    assert list(combinations(7, 3, [])) == [(1, 2, 4)]
    assert list(combinations(10, 2, [])) == [(1, 9), (2, 8), (3, 7), (4, 6)]
    assert list(combinations(10, 2, [1, 4])) == [(2, 8), (3, 7)]
