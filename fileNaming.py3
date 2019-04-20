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
