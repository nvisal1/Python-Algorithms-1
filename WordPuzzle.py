from collections import namedtuple
from itertools import product
import re
import sys
import timeit

Direction = namedtuple('Direction', 'di dj name')

DIRECTIONS = [
    Direction(-1, -1, "up and to the left"),
    Direction(-1,  0, "up"),
    Direction(-1, +1, "up and to the right"),
    Direction( 0, -1, "left"),
    Direction( 0, +1, "right"),
    Direction(+1, -1, "down and to the left"),
    Direction(+1,  0, "down"),
    Direction(+1, +1, "down and to the right"),
]

"""Reads the given file's contents as a 2D array.
:param filename: name of file to read
:type array: str
:returns: 2D array
:rtype: 2D array of file's contents
"""
def readPuzzleGrid(filename):
    with open(filename) as f:
        return [re.findall('[A-Z]', line.upper()) for line in f]
    
"""Reads the given file's contents as an array.
:param filename: name of file to read
:type array: str
:returns: array
:rtype: array of file's contents
"""
def readWordList(filename):
   text_file = open(filename, "r")
   lines = text_file.read().split('\n')
   return lines

"""Extract a word from the puzzle grid.
:param puzzleGrid: 2D array of scrambled words
:type puzzleGrid: 2D array
:param i: index of column
:type i: int
:param j: index of row
:type j: int
:param dir: array of directions
:type dir: array
:returns: word || None
:rtype: str
"""
def extract(puzzleGrid, i, j, dir):
    if ( 0 <= i + (length - 1) * dir.di < len(puzzleGrid) and
         0 <= j + (length - 1) * dir.dj < len(puzzleGrid[i]) ):
        return ''.join(
            puzzleGrid[i + n * dir.di][j + n * dir.dj] for n in range(length)
        )
    return None

"""Search the puzzle grid for a specific word.
:param puzzleGrid: 2D array of scrambled words
:type puzzleGrid: 2D array
:param word: word to search for
:type word: str
:returns: success message || None
:rtype: str
"""
def searchPuzzleGrid(puzzleGrid, word): 
    wordLength = len(word)
    for i, j, dir in product(range(len(puzzleGrid)), range(len(puzzleGrid[0])), DIRECTIONS):
        if word == extract(puzzleGrid, i, j, dir, wordLength):
            return "Found a match at line {0}, column {1} going {2}".format(
                i + 1, j + 1, dir.name)
    return None

"""Wrapper function to iterate through list of words and call searchPuzzleGrid().
:param puzzleGrid: 2D array of scrambled words
:type puzzleGrid: 2D array
:param wordList: list word to search for
:type wordList: array
:returns: message (success of failure)
:rtype: str
"""
def iterateWordList(puzzleGrid, wordList):
    resultMessages = []
    for word in wordList:
        match = searchPuzzleGrid(puzzleGrid, word.upper())
        if match is None:
            resultMessages.append('No match for the word ' + word)
            return resultMessages
        else:
            resultMessages.append('WORD: ' + word + ' --> ' + match)
    return resultMessages

"""Orchestrates the program.
:param puzzleFilename: filename of file that contains puzzle grid
:type puzzleFilename: str
:param wordListFilename: filename of file that contains list of words to search for
:type wordListFilename: str
"""
def main(puzzleFilename, wordListFilename):
    start = timeit.default_timer()
    puzzleGrid = readPuzzleGrid(puzzleFilename)
    wordList = readWordList(wordListFilename)
    searchResults = iterateWordList(puzzleGrid, wordList)
    for result in searchResults:
        print(result)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == '__main__':
    main('PuzzleInput.txt', 'WordList.txt')