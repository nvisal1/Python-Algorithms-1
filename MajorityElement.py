def method1(array) {
    for 
}

def method2(array) {

}

def method3(array) {

}

def readInput(filename):
    with open(filename) as f:
        return [re.findall('[A-Z]', line.upper()) for line in f]

def main(inputFilenames):
    puzzleGrid = readPuzzleGrid(puzzleFilename)
    wordList = readWordList(wordListFilename)
    searchResults = iterateWordList(puzzleGrid, wordList)
    for result in searchResults:
        print(result)

if __name__ == '__main__':
    main('PuzzleInput.txt', 'WordList.txt')