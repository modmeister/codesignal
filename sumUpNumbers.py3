def sumUpNumbers(inputString):
    numbers = []
    number = ""
    for c in inputString:
        if not c.isdigit() and number != "":
            numbers.append(int(number))
            number = ""
        elif c.isdigit():
            number += c
    if number != "": numbers.append(int(number))
    return sum(numbers)
