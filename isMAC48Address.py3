def isMAC48Address(inputString):
    codes = inputString.split('-')
    if len(codes) != 6: return False
    for code in codes:
        if not isHexDigit(code): return False
    return True
        
def isHexDigit(code):
    if len(code) != 2: return False
    hexvalues = "0123456789ABCDEFabcdef"
    return code[0] in hexvalues and code[1] in hexvalues
