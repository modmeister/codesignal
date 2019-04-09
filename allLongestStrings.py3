def allLongestStrings(inputArray):
    length = 0
    for input in inputArray:
        if len(input) > length:
            length = len(input)
    result = []
    for input in inputArray:
        if len(input) == length:
            result.append(input)
    return result
==================================
def allLongestStrings(inputArray):
    length = max(len(input) for input in inputArray)
    return [input for input in inputArray if len(input) == length]
