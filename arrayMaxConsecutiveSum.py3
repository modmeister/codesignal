def arrayMaxConsecutiveSum(inputArray, k):
    total = sum(inputArray[0:k])
    result = total
    for i in range(1, len(inputArray) - k + 1):
        total -= inputArray[i-1] - inputArray[i + k - 1]
        result = max(result, total)
    return result
