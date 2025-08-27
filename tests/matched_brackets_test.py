from project_program.matched_brackets import is_paired


def test_is_paired() -> None:
    assert is_paired("()") == True
    assert is_paired("([{}])") == True
    assert not is_paired("(]") == True
    assert not is_paired("([)]") == True
    assert not is_paired("())") == True
    assert is_paired("") == True
    assert is_paired("abc(123)[xyz]{456}") == True
    assert not is_paired("((((185 + 223.85) * 15) - 543)/2") == True
