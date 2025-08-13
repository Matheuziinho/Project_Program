from project_program.palindromic import max_palindrome, string_inverse


def test_string_inverse() -> None:
    assert "9009" == string_inverse(9_009)
    assert "1234321" == string_inverse(1_234_321)
    assert not "12331" == string_inverse(12_331)


def test_max_palindrome() -> None:
    assert max_palindrome(3) == 906_609
