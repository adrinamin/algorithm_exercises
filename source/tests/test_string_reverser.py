import unittest
from string_reverser.reverser import reverseWords


class PeekableIteratorTest(unittest.TestCase):    

    
    def test_reverse_three_words(self):
        input = "hello world here"
        expected = "here world hello"
        result = reverseWords(input)
        self.assertEqual(result, expected)
        
    
    def test_reverse_four_words(self):
        input = "hello my name is"
        expected = "is name my hello"
        result = reverseWords(input)
        self.assertEqual(result, expected)
        