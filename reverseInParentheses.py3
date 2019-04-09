def reverseInParentheses(inputString):
    while ('(' in inputString):
        head = inputString.rindex('(')
        tail = inputString.index(')', head + 1)
        sub = inputString[head:tail+1]
        rev = sub[::-1][1:-1]
        inputString = inputString.replace(sub, rev)
    return inputString
