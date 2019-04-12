def chessKnight(cell):
    counter = 0
    for i in range(-2, 3):
        if i == 0: continue
        x = ord(cell[0])
        y = int(cell[1])
        if i % 2 == 0:
            for j in range(-1,2,1):
                if j == 0: continue
                xMove = x + i
                yMove = y + j
                counter += checkMove(xMove, yMove)
        else:
            for j in range(-2,3,2):
                if j == 0: continue
                xMove = x + i
                yMove = y + j
                counter += checkMove(xMove, yMove)
    return counter

def checkMove(x, y):
    if 97 <= x <= 104 and 1 <= y <= 8:
        return 1
    return 0
