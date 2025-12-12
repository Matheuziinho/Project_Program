from project_program.change import find_fewest_coins


def test_find_fewest_coins() -> None:
    assert find_fewest_coins(0, [1, 2]) == []
    assert f
    assert find_fewest_coins(2, [1, 2]) == [2]
    assert find_fewest_coins(3, [1, 2, 5]) == [2, 1]
    assert find_fewest_coins(4, [1, 2, 5]) == [2, 2]
    assert find_fewest_coins(5, [1, 2, 5]) == [5]
    assert find_fewest_coins(20, [2, 5, 10]) == [10, 10]
    # assert find_fewest_coins(21, [2, 5, 10, 20, 50]) == [10, 5, 2, 2, 2]
    # assert find_fewest_coins(101, [2, 5, 10, 25]) == [25, 25, 25, 10, 10, 2, 2, 2]
    # assert find_fewest_coins(23, [1, 2, 5, 10, 20, 50]) == [20, 2, 1]
    # assert find_fewest_coins(94, [5, 10]) == ValueError("can't make target with given coins")
    # assert find_fewest_coins(-5, [1, 2, 5]) == ValueError("target can't be negative")
