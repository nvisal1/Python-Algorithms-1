from collections import namedtuple
from itertools import product
import re
import sys

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

def readPuzzleGrid(filename):
    with open(filename) as f:
        return [re.findall('[A-Z]', line.upper()) for line in f]
    
def readWordList(filename):
   text_file = open(filename, "r")
   lines = text_file.read().split('\n')
   return lines

def extract(grid, i, j, dir, length):
    if ( 0 <= i + (length - 1) * dir.di < len(grid) and
         0 <= j + (length - 1) * dir.dj < len(grid[i]) ):
        return ''.join(
            grid[i + n * dir.di][j + n * dir.dj] for n in range(length)
        )
    return None

def searchPuzzleGrid(puzzleGrid, word): 
    wordLength = len(word)
    for i, j, dir in product(range(len(puzzleGrid)), range(len(puzzleGrid[0])), DIRECTIONS):
        if word == extract(puzzleGrid, i, j, dir, wordLength):
            return "Found a match at line {0}, column {1} going {2}".format(
                i + 1, j + 1, dir.name)
    return None

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

def main(puzzleFilename, wordListFilename):
    puzzleGrid = readPuzzleGrid(puzzleFilename)
    wordList = readWordList(wordListFilename)
    searchResults = iterateWordList(puzzleGrid, wordList)
    for result in searchResults:
        print(result)

if __name__ == '__main__':
    main('PuzzleInput.txt', 'WordList.txt')