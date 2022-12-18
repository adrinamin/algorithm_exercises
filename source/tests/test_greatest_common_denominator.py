import unittest
from greatest_common_denominator import gcd

class GetGreatestCommonDenominator(unittest.TestCase):

    def test_get_greatest_common_denominator(self):
        result = gcd.get_greatest_common_denominator(6, 9)
        self.assertEqual(3, result)