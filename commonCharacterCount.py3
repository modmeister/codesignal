def commonCharacterCount(s1, s2):
    for c in s1:
        s2 = s2.replace(c, '_', 1)
    return s2.count('_')
