def isLucky(n):
    number = str(n)
    length = len(number)
    left = sum(int(digit) for digit in number[:length // 2])
    right = sum(int(digit) for digit in number[length // 2:])
    return left == right
===============
def isLucky(n):
    s = str(n)
    m = len(str(n)) // 2
    return sum(map(int, s[:m])) == sum(map(int, s)[m:])
