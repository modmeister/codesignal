def differentSquares(matrix):
    squares = []
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            square = (matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1], matrix[i][j])
            squares.append(square)
    return len(set(squares))
=============================
def differentSquares(matrix):
    squares = set()
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            square = (matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1], matrix[i][j])
            squares.add(square)
    return len(squares)
