"""Design and implement a HitCounter class that keeps track of requests (or hits). 
It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

"""
from datetime import datetime

class HitCounter:
    """initialize a HitCounter
    """
    def __init__(self):
      self.__hits = []
    
    """returns the total number of hits recorded
    """
    def total():
        return self.__hits


    def record(self, timestamp: float):
        """
        We append the timestamp to the list of hits
        
        :param timestamp: The current timestamp, which is an integer and guaranteed to be strictly
        increasing
        :type timestamp: float
        """
        self.__hits.append(timestamp)


    def total(self):
        """
        It returns the length of the list of hits.
        :return: The total number of hits.
        """
        return len(self.__hits)

    
    def range(self, lower: float, upper: float):
        """
        If the lower bound is greater than the first element in the array, or the upper bound is less
        than the last element in the array, return 0. Otherwise, return the number of elements in the
        array that are between the lower and upper bounds
        
        :param lower: The lower bound of the range
        :type lower: float
        :param upper: The upper bound of the range
        :type upper: float
        :return: The number of hits in the range.
        """
        
        maxHits = len(self.__hits) - 1

        for i in range(maxHits):
            if self.__hits[i] >= lower and self.__hits[maxHits - i] <= upper:
                return maxHits + 1 - i


def main():
    pass


if __name__ == '__main__':
    main()