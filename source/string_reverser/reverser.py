import traceback

class PeekableIterator(object):
    c = 0
    def __init__(self, iterator):
        self.max = sum(1 for element in iterator)


    def __iter__(self):
        self.n = 0
        return self


import sys


def reverseWords(wordstring: str):
    words = wordstring.split(" ")
    reversedWords = __reverse(words)
    result = ""
    for index, word in enumerate(reversedWords):
        if index == 0:
            result += word
        else:    
            result += " " + word
        
    return result


def __reverse(words: list):
    return words


def main(wordstring: str):
    return reverseWords(wordstring)
    

if __name__ == '__main__':
    main(sys.argv[1])