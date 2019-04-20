def fileNaming(names):
    while len(set(names)) != len(names):
        for i in range(len(names)):
            level = 1
            for j in range(len(names)):
                if i == j: 
                    continue
                if names[i] == names[j]:
                    new = names[i] + "(" + str(level) + ")"
                    while new in names[:j]:
                        level += 1
                        new = names[i] + "(" + str(level) + ")"
                    names[j] = new
    return names
======================
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            o = 1
            while names[i] + "(" + str(o) + ")" in names[:i]:
                o += 1
            names[i] += "(" + str(o) + ")"
    return names
