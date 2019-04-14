def validTime(time):
    values = time.split(':')
    if len(values) != 2: return False
    if 0 <= int(values[0]) <= 23 and 0 <= int(values[1]) <= 59: return True
    return False
====================
def validTime(time):
    h, m = map(int, time.split(':'))
    return 0 <= h <= 23 and 0 <= m <= 59
