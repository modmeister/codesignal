def validTime(time):
    values = time.split(':')
    if len(values) != 2: return False
    if 0 <= int(values[0]) <= 23 and 0 <= int(values[1]) <= 59: return True
    return False
