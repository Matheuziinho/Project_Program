from class_exercises.palindromic import string_inversa,max_palindromo

def test_string_inversa() -> None:
    assert string_inversa(9_009)
    assert string_inversa(1_234_321)
    assert not string_inversa(12_331)

def test_max_palindromo() -> None:
    assert max_palindromo(3) == 906609

