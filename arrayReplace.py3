def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray
==============================================================
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if value == elemToReplace else value for value in inputArray]
