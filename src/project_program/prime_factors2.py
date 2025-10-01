# Prime Factors
# Compute the prime factors of a given natural number.


class PrimeFactors:
    def __init__(self, number: int) -> None:
        self.number = number

    def prime_factors(self) -> list[int]:
        factors = []
        number = self.number
        divisor = 2
        while number > 1:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                divisor += 1
        return factors
