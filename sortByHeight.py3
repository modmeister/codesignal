def sortByHeight(a):
    b = [x for x in a if x > -1]
    b.sort()
    for i in range(len(a)):
        if a[i] > -1:
            a[i] = b.pop(0)
    return a
