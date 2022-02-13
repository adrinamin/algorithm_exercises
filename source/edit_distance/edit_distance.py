"""
edit_distane.py

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
"""
import sys

def calculate_edit_distance(string1: str, string2: str):
    """Calculates the edit distance between two strings.

    Args:
        string1 (str): the first string.
        string2 (str): the second string.
    """
    editDistance = 0
    if len(string1) != len(string2):
        editDistance = abs(len(string1) - len(string2))
        
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            editDistance += 1
    
    return editDistance

def main(string1: str, string2: str):
    """ Main function.

    Args:
        string1 (str): the first string.
        string2 (str): the second string.
    """
    editDistance = calculate_edit_distance(string1, string2)
    print("The edit distance between", string1, "and", string2, "is", editDistance)
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])