def lineEncoding(s):
    sample = s[0]
    counter = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == sample:
            counter += 1
        elif counter == 1:
            result += sample
        else:
            result += str(counter) + sample
            counter = 1
        sample = s[i]
    if counter == 1:
        result += sample
    else:
        result += str(counter) + sample
    return result
