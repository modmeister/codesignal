def alphabeticShift(inputString):
    result = ""
    for c in inputString:
        if c == 'z': result += 'a'
        else: result += chr(ord(c) + 1)
    return result
