def adjacentElementsProduct(inputArray):
    result = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        result = max(result, inputArray[i] * inputArray[i+1])
    return result
========================================
def adjacentElementsProduct(inputArray):
    return max(inputArray[i] * inputArray[i+1] for i in range(len(inputArray) - 1))
