# Pythagorean triplet


class Product:
    def pythagorean(self, target: int, n: int, m: int) -> int:
        if m <= n or n <= 0:
            return 0

        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        if a + b + c != target:
            return 0

        return a * b * c
