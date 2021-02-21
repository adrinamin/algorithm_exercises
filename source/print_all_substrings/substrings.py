import sys


def get_substrings(source: str):
    """Get all substrings of a given string

    Args:
        string (str): the string to generate the substring from

    Returns:
        list: list of substrings
    """ 
    # the number of substrings per length is the same as the length of the substring
    # if the characters are not equal. For each duplicate char decrease number of substrings by 1
    
    
    substrings = []
    # for i in range(len(source)):
    s = ""
    for j in range(len(source)):
        substrings.append(source[j])
        s += source[j]
    substrings.append(s)

    return substrings


def main(string: str):
    substrings = get_substrings(str)
    print(substrings)
    

if __name__ == "__main__":
    main(sys[0])