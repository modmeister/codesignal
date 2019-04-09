def alternatingSums(a):
    b = [0 ,0]
    for i in range(len(a)):
        b[i % 2] += a[i]
    return b
=======================
def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]
