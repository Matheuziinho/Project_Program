from project_program.rotational_cipher import rotate_chars


def test_rotational_cipher():
    assert rotate_chars("a", 26) == "a"
    assert rotate_chars("m", 13) == "z"
    assert rotate_chars("n", 13) == "a"
    assert rotate_chars("a", 0) == "a"
    assert rotate_chars("a", 25) == "z"
    assert rotate_chars("hello", 13) == "uryyb"
    assert rotate_chars("Hello, world!", 13) == "Uryyb, jbeyq!"
    assert (
        rotate_chars("The quick brown fox jumps over the lazy dog.", 13)
        == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
    )
