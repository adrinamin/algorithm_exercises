import unittest
import random_number_generator.rand as rand


class RandomNumberCreator(unittest.TestCase):
    
    def test_rand7(self):
        result = rand.rand7()
        self.assertGreater(result, abs(0))
        
    
    def test_rand5(self):
        result = rand.rand5()
        self.assertGreater(result, abs(0))
        
        
if __name__ == '__main__':
    unittest.main()
    