import unittest

from project_program.series import Series


class SeriesTest(unittest.TestCase):
    def test_slices_of_one_from_one(self):
        self.assertEqual(Series("1").slices(1), ["1"])
        pass

    def test_slices_of_one_from_two(self):
        self.assertEqual(Series("12").slices(1), ["1", "2"])
        pass

    def test_slices_of_two_from_one(self):
        self.assertEqual(Series("35").slices(2), ["35"])
        pass

    def test_slices_of_two_overlap(self):
        self.assertEqual(Series("9142").slices(2), ["91", "14", "42"])
        pass

    def test_slices_can_include_duplicates(self):
        self.assertEqual(Series("777777").slices(3), ["777", "777", "777", "777"])
        pass

    def test_slices_of_a_long_series(self):
        self.assertEqual(
            Series("918493904243").slices(5),
            ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"],
        )
        pass

    def test_slice_length_is_too_large(self):
        with self.assertRaises(ValueError) as err:
            Series("12345").slices(6)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "Slice length cannot be greater than series length."
        )
        pass

    def test_slice_length_is_way_too_large(self):
        with self.assertRaises(ValueError) as err:
            Series("12345").slices(42)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "Slice length cannot be greater than series length."
        )
        pass

    def test_slice_length_cannot_be_zero(self):
        with self.assertRaises(ValueError) as err:
            Series("12345").slices(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Slice length cannot be zero.")
        pass

    def test_slice_length_cannot_be_negative(self):
        with self.assertRaises(ValueError) as err:
            Series("123").slices(-1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Slice length cannot be negative.")
        pass

    def test_empty_series_is_invalid(self):
        with self.assertRaises(ValueError) as err:
            Series("").slices(1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Series cannot be empty.")
        pass
