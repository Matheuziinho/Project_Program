import unittest

from project_program.hamming import HammingTest


class TestHamming(unittest.TestCase):
    def test_empty_strands(self):
        hamming = HammingTest("")
        self.assertEqual(hamming.distance(""), 0)

    def test_single_letter_identical_strands(self):
        hamming = HammingTest("A")
        self.assertEqual(hamming.distance("A"), 0)

    def test_single_letter_different_strands(self):
        hamming = HammingTest("G")
        self.assertEqual(hamming.distance("T"), 1)

    def test_long_identical_strands(self):
        hamming = HammingTest("GGACTGAAATCTG")
        self.assertEqual(hamming.distance("GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        hamming = HammingTest("GGACGGATTCTG")
        self.assertEqual(hamming.distance("AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        hamming = HammingTest("AATG")
        with self.assertRaises(ValueError) as err:
            hamming.distance("AAA")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_second_strand_longer(self):
        hamming = HammingTest("ATA")
        with self.assertRaises(ValueError) as err:
            hamming.distance("AGTG")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_empty_first_strand(self):
        hamming = HammingTest("")
        with self.assertRaises(ValueError) as err:
            hamming.distance("G")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")

    def test_disallow_empty_second_strand(self):
        hamming = HammingTest("G")
        with self.assertRaises(ValueError) as err:
            hamming.distance("")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Strands must be of equal length.")
