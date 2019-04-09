def areSimilar(a, b):
    if a == b: return True
    if set(a) != set(b): return False
    c = []
    for i in range(len(a)):
        if a[i] != b[i]:
            c.append(i)
    if len(c) != 2: return False
    return a[c[0]] == b[c[1]] and a[c[1]] == b[c[0]]
