import re

# def method1(array):

# def method2(array):

# def method3(array):

def readInputFile(filename):
    with open(filename) as textFile:
        lines = [line.split() for line in textFile]
    return lines

def main(inputFilenames):
    for index, inputFilename in enumerate(inputFilenames):
        result = readInputFile(inputFilename)

if __name__ == '__main__':
    main(['Majex1.txt', 'Majex2.txt', 'Majex3.txt', 'Majex4.txt'])