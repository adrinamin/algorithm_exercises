import unittest
from print_all_substrings.substrings import get_substrings


class GetSubstringTests(unittest.TestCase):
    
    # def test_get_all_substrings_three_chars(self):
    #     self.assertEqual(["x","y","z","xy","yz","xyz"],get_substrings("xyz"))
        
    def test_get_all_substrings_two_chars(self):
        self.assertEqual(["x","y","xy"],get_substrings("xy"))