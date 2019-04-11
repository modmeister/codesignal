def alphabeticShift(inputString):
    result = ""
    for c in inputString:
        if c == 'z': result += 'a'
        else: result += chr(ord(c) + 1)
    return result
=================================
def alphabeticShift(inputString):
    return ''.join(chr(ord(c) + 1) if c != 'z' else 'a' for c in inputString)
