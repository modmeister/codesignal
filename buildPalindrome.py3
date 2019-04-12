def buildPalindrome(st):
    for i in range(len(st)):
        if st[i:] in st[::-1]:
            return st[:i] + st[::-1]
