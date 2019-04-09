def addBorder(picture):
    width = len(picture[0]) + 2
    height = len(picture)
    for i in range(height):
        picture[i] = '*' + picture[i] + '*'
    picture.insert(0, '*' * width)
    picture.append('*' * width)
    return picture
=======================
def addBorder(picture):
    return ['*' * (len(picture[0]) + 2)] + ['*' + line + '*' for line in picture] + ['*' * (len(picture[0]) + 2)]
