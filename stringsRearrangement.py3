from itertools import permutations

def stringsRearrangement(inputArray):
    cases = list(permutations(inputArray))
    for case in cases:
        for i in range(1, len(case)):
            flag = 0
            first = case[i-1]
            second = case[i]
            for j in range(len(first)):
                if first[j] != second[j]:
                    flag += 1
                    if flag > 1: 
                        break
            if flag != 1: 
                break
            if i == len(case) - 1 and flag == 1:
                return True
    return False
