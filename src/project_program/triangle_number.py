# Highly divisible triangular number


def triangular_number(terms: int) -> int:
    return (terms * (terms + 1)) // 2
