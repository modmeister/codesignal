def variableName(name):
    if name[0].isdigit(): return False
    for c in name:
        if not c.isalnum() and not c == '_':
            return False
    return True
