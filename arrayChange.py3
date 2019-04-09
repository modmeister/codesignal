def arrayChange(inputArray):
    result = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] > inputArray[i-1]:
            continue
        else:
            change = inputArray[i-1] - inputArray[i] + 1
            inputArray[i] += change
            result += change
    return result
