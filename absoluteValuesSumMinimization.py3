def absoluteValuesSumMinimization(a):
    smallest = sum(abs(a[0] - x) for x in a)
    index = 0
    for i, x in enumerate(a):
        total = sum(abs(y - x) for y in a)
        if total < smallest:
            index = i
            smallest = total
    return a[index]
=====================================
def absoluteValuesSumMinimization(a):
    return a[(len(a) - 1) // 2]
