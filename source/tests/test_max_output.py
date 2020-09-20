import unittest
from max_power_output.max_p_out_calc import maxProduct


class MaxOutputTests(unittest.TestCase):
    
    def test_maximum_panel_output(self):
        arr = [-2,-3,4,-5]
        result = maxProduct(arr)
        self.assertEqual(result, "60")
        
    def test_maximum_panel_output8(self):
        arr = [2,0,2,2,0]
        result = maxProduct(arr)
        self.assertEqual(result, "8")
        
    def test_maximum_panel_output_high_number(self):
        arr = [1000,-100,200,50,-300,40,-3]
        result = maxProduct(arr)
        self.assertEqual(result, "12000000000000")
        
    
    def test_maximum_panel_output_negativ_numbers(self):
        arr = [-40,-100,-1000,-200,-50,-300,-3]
        result = maxProduct(arr)
        self.assertEqual(result, "12000000000000")
        
        
    def test_maximum_panel_output_higher_number(self):
        arr = [1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300,1000,-100,200,50,-300]
        result = maxProduct(arr)
        self.assertEqual(result, "19683000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        
    def test_maximum_panel_output_zero(self):
        arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        result = maxProduct(arr)
        self.assertEqual(result, "0")
        
    def test_maximum_panel_output_thousand(self):
        arr = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
        result = maxProduct(arr)
        self.assertEqual(result, "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        
    def test_maximum_panel_output_one(self):
        arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        result = maxProduct(arr)
        self.assertEqual(result, "1")