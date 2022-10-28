import unittest
from overlapping_rectangles import overlap


class RectanglesOverlapTest(unittest.TestCase):

    def test_two_identical_rectangles_overlap(self):
        rectangles = [overlap.Rect((0, 0), (1, 1)), overlap.Rect((0, 0), (1, 1))]
        self.assertTrue(overlap.checkOverlapping(rectangles))

    
    def test_two_partly_identical_rectangles_overlap(self):
        rectangles = [overlap.Rect((1,4), (3,3)), overlap.Rect((0,5), (4,3))]
        self.assertTrue(overlap.checkOverlapping(rectangles))

    
    def test_first_rectangle_starting_point_smaller(self):
        rectangles = [overlap.Rect((0,2), (2,2)), overlap.Rect((1,1), (2,2))]
        self.assertTrue(overlap.checkOverlapping(rectangles))

    
    def test_first_rectangle_starting_point_smaller_no_overlap(self):
        rectangles = [overlap.Rect((0,2), (1,1)), overlap.Rect((1,1), (2,2))]
        self.assertFalse(overlap.checkOverlapping(rectangles))


    def test_three_rectangles_and_two_rectangles_overlap(self):
        rectangles = [overlap.Rect((0,2), (2,2)), overlap.Rect((2,3), (1,1)), overlap.Rect((1,1), (2,2))]
        self.assertTrue(overlap.checkOverlapping(rectangles))


    def test_three_different_rectangles_and_two_rectangles_overlap(self):
        rectangles = [overlap.Rect((1,4), (3,3)), overlap.Rect((-1, 3), (2,1)), overlap.Rect((0,5), (4,3))]
        self.assertTrue(overlap.checkOverlapping(rectangles))


if __name__ == '__main__':
    unittest.main()
