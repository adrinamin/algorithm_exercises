import unittest
import square_and_sort.sas as square_and_sort


class SquareAndSortArrayTests(unittest.TestCase):
    
    def test_square_and_sort_elements(self):
        input = [-9, -2, 0, 2, 3]
        expected = [0, 4, 4, 9, 81]
        result = square_and_sort.squareAndSortElements(input)
        self.assertEqual(expected, result)
        
        
    def test_square_and_sort_elements_with_seven_elements(self):
        input = [-9, -2, 0, 2, -3, 5, 3]
        expected = [0, 4, 4, 9, 9, 25, 81]
        result = square_and_sort.squareAndSortElements(input)
        self.assertEqual(expected, result)