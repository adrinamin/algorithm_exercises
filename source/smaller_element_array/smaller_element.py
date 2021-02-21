""" smaller_element.py module which returns a new array 
where each element in the new array is then number 
of smaller elements to the right of that element 
in the original input array.

Usage: 

    python3 smaller_element.py <input_array>
"""

import sys

def get_smaller_element_array(input_array:list):
    result = []
    
    if len(input_array) == 1:
        result.append(0)
        return result
    
    first = input_array.pop(0)
        
    t = 0
    for i in input_array:
        if first > i:
            t += 1
    result.append(t)
    x = get_smaller_element_array(input_array)
    result.extend(x)
    
    return result
            

def main(input_array:list):
    """ Calls the method for getting the new array
    
    Keyword arguments:
    input_array: An array with integers.
    Return: The new array with the number of smaller elements
    to the right of each element.
    """
    result = get_smaller_element_array(input_array)
    print("new array with smaller elements"+
          " to the right of each element: ", result)