import unittest

from project_program.prime_factors2 import PrimeFactors


class PrimePrimeFactorsTest(unittest.TestCase):
    def test_no_PrimeFactors(self):
        self.assertEqual(PrimeFactors(1).prime_factors(), [])

    def test_prime_number(self):
        self.assertEqual(PrimeFactors(2).prime_factors(), [2])

    def test_another_prime_number(self):
        self.assertEqual(PrimeFactors(3).prime_factors(), [3])

    def test_square_of_a_prime(self):
        self.assertEqual(PrimeFactors(9).prime_factors(), [3, 3])

    def test_product_of_first_prime(self):
        self.assertEqual(PrimeFactors(4).prime_factors(), [2, 2])

    def test_cube_of_a_prime(self):
        self.assertEqual(PrimeFactors(8).prime_factors(), [2, 2, 2])

    def test_product_of_second_prime(self):
        self.assertEqual(PrimeFactors(27).prime_factors(), [3, 3, 3])

    def test_product_of_third_prime(self):
        self.assertEqual(PrimeFactors(625).prime_factors(), [5, 5, 5, 5])

    def test_product_of_first_and_second_prime(self):
        self.assertEqual(PrimeFactors(6).prime_factors(), [2, 3])

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(PrimeFactors(12).prime_factors(), [2, 2, 3])

    def test_product_of_primes(self):
        self.assertEqual(PrimeFactors(901_255).prime_factors(), [5, 17, 23, 461])

    def test_PrimeFactors_include_a_large_prime(self):
        self.assertEqual(
            PrimeFactors(93_819_012_551).prime_factors(), [11, 9_539, 894_119]
        )
