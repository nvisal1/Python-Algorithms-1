"""Recursive function to convret a given decimal to binary.
:param decimal: decimal to convert to binary
:type decimal: str
:returns: error string or binary string
:rtype: str
"""
def decimalToBinary(decimal):
    if decimal < 0:
        return 'Decimal must be a positive integer'
    elif decimal == 0:
        return '0'; 
    else: 
        return decimalToBinary(decimal//2) + str(decimal%2)

number = input('Enter a decimal')
result = decimalToBinary(number)
print('Binary representation: ' + result)