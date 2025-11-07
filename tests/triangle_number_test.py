import unittest

from project_program.triangle_number import triangular_number


class TriangularTest(unittest.TestCase):
    def test_triangular_number(self) -> None:
        self.assertEqual(triangular_number(500), 125_250)
