"""
Name: Nicholas Visalli 
Assignment number: 1
Purpose: Design 3 algorithms to find the majority element of an array
"""

import re

"""(O(N^2)) algorithm to find majority element within an array.
:param array: array of numbers between 1 - 9
:type array: array
:returns: None || majority element
:rtype: int
"""
def method1(array):
    arrayFlat = sum(array, [])
    halfLength = len(arrayFlat)//2
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
            if dictionary[array[i][j]] > halfLength:
                return array[i][j]
    return None

"""(O(NlogN)) algorithm to find majority element within an array.
:param array: array of numbers between 1 - 9
:type array: array
:returns: None || majority element
:rtype: int
"""
def method2(array):
    if len(array) == 1:
        return array[0]
    halfLength = len(array)//2

    firstResult = method2(array[:halfLength])
    secondResult = method2(array[halfLength:])

    if firstResult == secondResult:
        return firstResult

    lcount = array.count(firstResult)
    rcount = array.count(secondResult)

    if lcount > halfLength:
        return firstResult
    elif rcount > halfLength:
        return secondResult
    else: 
        return None
    
"""(O(N)) algorithm to find majority element within an array.
:param array: array of numbers between 1 - 9
:type array: array
:returns: None || majority element
:rtype: int
"""
def method3(array):
    # Method 3 step 1
    halfLength = len(array)//2
    majIndex = 0
    count = 0
    for i in range(len(array)):
        if array[majIndex] == array[i]:
            count += 1
        else: 
            count -= 1
        if count == 0:
            majIndex = i
            count = 1
    # Method 3 step 2
    check = array.count(array[majIndex])
    if (check > halfLength):
        return array[majIndex]
    else:
        return "Found " + array[majIndex] + ", but it does not match"

"""Converts contents of text file to a 2D array.
:param filename: name of the file to read
:type filename: str
:returns: lines
:rtype: 2D array
"""
def readInputFile(filename):
    with open(filename) as textFile:
        lines = [line.split() for line in textFile]
    return lines

"""Orchestrates the program.
:param inputFilenames: array of all file names to read
:type inputFillenames: array
"""
def main(inputFilenames):
    for index, inputFilename in enumerate(inputFilenames):
        array2D = readInputFile(inputFilename)
        arrayFlat = sum(array2D, [])
        method1Result = method1(array2D)
        print("********************")
        print('Method 1')
        print('Filename: ' + inputFilename)
        print('Result: ')
        print(method1Result)
        print("====================")
        method2Result = method2(arrayFlat)
        print('Method 2')
        print('Filename: ' + inputFilename)
        print('Result: ')
        print(method2Result)
        print("====================")
        method3Result = method3(arrayFlat)
        print('Method 3')
        print('Filename: ' + inputFilename)
        print('Result: ')
        print(method3Result)
        print("********************")
        print('')

if __name__ == '__main__':
    main(['Majex1.txt', 'Majex2.txt', 'Majex3.txt', 'Majex4.txt'])