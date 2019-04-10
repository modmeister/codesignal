def avoidObstacles(inputArray):
    range = 2
    inputArray.sort()
    position = range
    while (position <= inputArray[-1]):
        if position in inputArray:
            range += 1
            position = range
            continue
        position += range
    return range
