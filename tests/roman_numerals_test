import unittest

from project_program.roman_numerals import transformation


class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_i(self):
        self.assertEqual(transformation(1), "I")

    def test_2_is_ii(self):
        self.assertEqual(transformation(2), "II")

    def test_3_is_iii(self):
        self.assertEqual(transformation(3), "III")

    def test_4_is_iv(self):
        self.assertEqual(transformation(4), "IV")

    def test_5_is_v(self):
        self.assertEqual(transformation(5), "V")

    def test_6_is_vi(self):
        self.assertEqual(transformation(6), "VI")

    def test_9_is_ix(self):
        self.assertEqual(transformation(9), "IX")

    def test_16_is_xvi(self):
        self.assertEqual(transformation(16), "XVI")

    def test_27_is_xxvii(self):
        self.assertEqual(transformation(27), "XXVII")

    def test_48_is_xlviii(self):
        self.assertEqual(transformation(48), "XLVIII")

    def test_49_is_xlix(self):
        self.assertEqual(transformation(49), "XLIX")

    def test_59_is_lix(self):
        self.assertEqual(transformation(59), "LIX")

    def test_66_is_lxvi(self):
        self.assertEqual(transformation(66), "LXVI")

    def test_93_is_xciii(self):
        self.assertEqual(transformation(93), "XCIII")

    def test_141_is_cxli(self):
        self.assertEqual(transformation(141), "CXLI")

    def test_163_is_clxiii(self):
        self.assertEqual(transformation(163), "CLXIII")

    def test_166_is_clxvi(self):
        self.assertEqual(transformation(166), "CLXVI")

    def test_402_is_cdii(self):
        self.assertEqual(transformation(402), "CDII")

    def test_575_is_dlxxv(self):
        self.assertEqual(transformation(575), "DLXXV")

    def test_666_is_dclxvi(self):
        self.assertEqual(transformation(666), "DCLXVI")

    def test_911_is_cmxi(self):
        self.assertEqual(transformation(911), "CMXI")

    def test_1024_is_mxxiv(self):
        self.assertEqual(transformation(1024), "MXXIV")

    def test_1666_is_mdclxvi(self):
        self.assertEqual(transformation(1666), "MDCLXVI")

    def test_3000_is_mmm(self):
        self.assertEqual(transformation(3000), "MMM")

    def test_3001_is_mmmi(self):
        self.assertEqual(transformation(3001), "MMMI")

    def test_3888_is_mmmdccclxxxviii(self):
        self.assertEqual(transformation(3888), "MMMDCCCLXXXVIII")

    def test_3999_is_mmmcmxcix(self):
        self.assertEqual(transformation(3999), "MMMCMXCIX")
