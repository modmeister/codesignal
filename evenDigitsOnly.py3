def evenDigitsOnly(n):
    return all(int(c) % 2 == 0 for c in str(n))
