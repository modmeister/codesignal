def almostIncreasingSequence(sequence):
    flag = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            flag += 1
            if flag > 1:
                return False
            if i > 1 and i < len(sequence) - 1:
                if sequence[i] <= sequence[i-2] and sequence[i+1] <= sequence[i-1]:
                    return False
    return True
