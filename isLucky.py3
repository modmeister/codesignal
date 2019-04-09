def isLucky(n):
    number = str(n)
    length = len(number)
    left = sum(int(digit) for digit in number[:length // 2])
    right = sum(int(digit) for digit in number[length // 2:])
    return left == right
