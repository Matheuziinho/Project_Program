import unittest

from project_program.pythagorean_triplet import Product


class TestProduct(unittest.TestCase):

    def test_product_for_1000(self) -> None:
        self.assertEqual(Product().pythagorean(1000, 200, 375), 31875000)
