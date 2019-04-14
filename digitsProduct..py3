def digitsProduct(product):
    if product == 0: return 10
    if 1 <= product <= 9: return product
    result = ""
    i = 9
    while (product != 0):
        if product % i == 0:
            product //= i
            result = str(i) + result
            continue
        i -= 1
        if i == 1:
            if product > 10: return -1
            break
    if product > 9 and result == '': return -1
    return int(result)
