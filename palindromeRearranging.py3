def palindromeRearranging(inputString):
    characters = set(inputString)
    flag = 0
    for character in characters:
        if inputString.count(character) % 2 != 0:
            flag += 1
            if flag > 1:
                return False
    return True
