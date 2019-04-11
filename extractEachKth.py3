def extractEachKth(inputArray, k):
    return [inputArray[i] for i in range(len(inputArray)) if (i + 1) % k != 0]
==================================
def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray
