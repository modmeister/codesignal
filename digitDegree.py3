def digitDegree(n):
    n = str(n)
    l = len(n)
    if l == 1: return 0
    s = sum(int(d) for d in n)
    c = 1
    while(s > 9):
        n = str(s)
        s = sum(int(d) for d in n)
        c += 1
    return c
===================
def digitDegree(n):
    c = 0
    while (n >= 10):
        n = sum(int(d) for d in str(n))
        c += 1
    return c
