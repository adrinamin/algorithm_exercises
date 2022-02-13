import unittest
import edit_distance.edit_distance as ed

class EditDistanceTest(unittest.TestCase):
    
    def test_edit_distance_with_same_string(self):
        self.assertEqual(ed.calculate_edit_distance("abc", "abc"), 0)
        
    def test_edit_distance_with_different_string(self):
        self.assertEqual(ed.calculate_edit_distance("abc", "abd"), 1)
        
if __name__ == '__main__':
    unittest.main()