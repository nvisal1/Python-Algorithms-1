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
                return array[i][j], dictionary.get(array[i][j])
    return None

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
    
def method3(array):
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
    return array[majIndex]

def readInputFile(filename):
    with open(filename) as textFile:
        lines = [line.split() for line in textFile]
    return lines

def main(inputFilenames):
    for index, inputFilename in enumerate(inputFilenames):
        result = readInputFile(inputFilename)
        method1Result = method1(result)
        print(method1Result)
        print("====================")
        method2Result = method2(result)
        print(method2Result)
        print("====================")
        method3Result = method3(result)
        print(method3Result)

if __name__ == '__main__':
    main(['Majex1.txt', 'Majex2.txt', 'Majex3.txt', 'Majex4.txt'])