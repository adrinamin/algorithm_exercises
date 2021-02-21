import unittest
import smaller_element_array.smaller_element as smaller_element


class SmallerElementTest(unittest.TestCase):
    
    def test_get_smaller_element_array_basic(self):
        input_array=[3,4,9,6,1]
        expected = [1,1,2,1,0]
        result = smaller_element.get_smaller_element_array(input_array)
        self.assertEqual(expected, result)
        
    def test_get_smaller_element_array_advanced(self):
        input_array=[4,2,10,8,5,3,12]
        expected = [2,0,3,2,1,0,0]
        result = smaller_element.get_smaller_element_array(input_array)
        self.assertEqual(expected, result)