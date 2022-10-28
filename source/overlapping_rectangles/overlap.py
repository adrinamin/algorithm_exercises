"""Compute whether or not a pair of rectangles overlap each other. 
If one rectangle completely covers another, it is considered overlapping.

"""

class Rect:
    def __init__(self, top_left, dimensions):
        self.top_left = top_left
        self.dimensions = dimensions

def checkOverlapping(rectangles: list):
    """Check whether or not a list of rectangles overlap each other

    Args:
        rectangles (list): a list of rectangles to check

    Returns:
        boolean: true if a pair of rectangles overlap each other, otherwise false
    """

    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if rectangles[i].top_left == rectangles[j].top_left and rectangles[i].dimensions == rectangles[j].dimensions:
                return True
            elif rectangles[i].top_left[0] > rectangles[j].top_left[0] and rectangles[i].dimensions[0] < rectangles[j].dimensions[0]:
                return True
            elif rectangles[i].top_left[0] < rectangles[j].top_left[0] and rectangles[i].dimensions[0] == rectangles[j].dimensions[0]:
                return True
    
    return False


def main():
    rectangles = [Rect((1,4), (3,3)), Rect((-1, 3), (2,1)), Rect((0,5), (4,3))]
    result = checkOverlapping(rectangles)
    print(result)

if __name__ == '__main__':
   main()
