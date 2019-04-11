def longestDigitsPrefix(inputString):
    if not inputString[0].isdigit(): return ""
    result = str(inputString[0])
    for i in range(1, len(inputString)):
        if not inputString[i].isdigit(): return result
        result += inputString[i]
    return result
