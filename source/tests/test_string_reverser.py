import unittest
from string_reverser.reverser import reverseWords


class PeekableIteratorTest(unittest.TestCase):    
    # def setUp(self):

    
    def test_reverse_words(self):
        input = "hello world here"
        expected = "here world hello"
        result = reverseWords(input)
        self.assertEqual(result, expected)
        