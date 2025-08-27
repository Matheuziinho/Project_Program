from project_program.ten_thousand_one_prime import is_prime, th_prime


def test_th_prime():
    assert is_prime(13) == True
    assert is_prime(45) == False
    assert th_prime(6) == 13
    assert th_prime(10001) == 104743
