def circleOfNumbers(n, firstNumber):
    if firstNumber < n // 2: return firstNumber + n // 2
    return firstNumber - n // 2
====================================
def circleOfNumbers(n, firstNumber):
    return firstNumber + n // 2 if firstNumber < n // 2 else firstNumber - n // 2
====================================
def circleOfNumbers(n, firstNumber):
    return (firstNumber + n // 2) % n
