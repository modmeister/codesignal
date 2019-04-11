def arrayMaxConsecutiveSum(inputArray, k):
    total = sum(inputArray[0:k])
    result = total
    for i in range(1, len(inputArray) - k + 1):
        total -= inputArray[i-1] - inputArray[i + k - 1]
        result = max(result, total)
    return result
==========================================
def arrayMaxConsecutiveSum(inputArray, k):
    total = result = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        total += inputArray[i + k] - inputArray[i]
        result = max(result, total)
    return result
