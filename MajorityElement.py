import re

def method1(array):
    halfLength = len(array)//2
    dictionary = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0, 
        '8': 0,
        '9': 0,
    }

    for i in range(len(array)):
        for j in range(len(array[i])):
            dictionary[array[i][j]] = dictionary.get(array[i][j]) + 1
            if dictionary[array[i][j]] >= halfLength:
                return array[i][j]
    return None

# def method2(array):

# def method3(array):

def readInputFile(filename):
    with open(filename) as textFile:
        lines = [line.split() for line in textFile]
    return lines

def main(inputFilenames):
    for index, inputFilename in enumerate(inputFilenames):
        result = readInputFile(inputFilename)
        method1Result = method1(result)
        print(method1Result)

if __name__ == '__main__':
    main(['Majex1.txt', 'Majex2.txt', 'Majex3.txt', 'Majex4.txt'])