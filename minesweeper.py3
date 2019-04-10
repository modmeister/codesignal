def minesweeper(matrix):
    width = len(matrix[0])
    height = len(matrix)

    result = [[0 for i in range(width)] for j in range(height)]
    
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == True:
                if i == 0 and j == 0 and width > 1 and height > 1:
                    print("TopLeft")
                    result[0][1] += 1
                    result[1][0] += 1
                    result[1][1] += 1
                if i == 0 and j == width - 1 and width > 1 and height > 1:
                    print("TopRight")
                    result[0][j-1] += 1
                    result[1][j-1] += 1
                    result[1][j] += 1
                if i == height - 1 and j == 0 and width > 1 and height > 1:
                    print("BottomLeft")
                    result[i-1][0] += 1
                    result[i-1][1] += 1
                    result[i][1] += 1
                if i == height - 1 and j == width - 1 and width > 1 and height > 1:
                    print("BottomRight")
                    result[i-1][j] += 1
                    result[i-1][j-1] += 1
                    result[i][j-1] += 1
                if i == 0 and 0 < j < width - 1 and width > 2 and height > 1:
                    print("MiddleTop")
                    result[0][j-1] += 1
                    result[1][j-1] += 1
                    result[1][j] += 1
                    result[1][j+1] += 1
                    result[0][j+1] += 1
                if 0 < i < height - 1 and j == 0 and width > 1 and height > 2:
                    print("MiddleLeft")
                    result[i-1][0] += 1
                    result[i-1][1] += 1
                    result[i][1] += 1
                    result[i+1][1] += 1
                    result[i+1][0] += 1
                if i == height - 1 and 0 < j < width - 1 and width > 2 and height > 1:
                    print("MiddleBottom")
                    result[i][j-1] += 1
                    result[i-1][j-1] += 1
                    result[i-1][j] += 1
                    result[i-1][j+1] += 1
                    result[i][j+1] += 1
                if 0 < i < height - 1 and j == width - 1 and width > 1 and height > 2:
                    print("MiddleRight")
                    result[i-1][j] += 1
                    result[i-1][j-1] += 1
                    result[i][j-1] += 1
                    result[i+1][j-1] += 1
                    result[i+1][j] += 1
                if 0 < i < height - 1 and 0 < j < width - 1 and width > 2 and height > 2:
                    print("MiddleMiddle")
                    result[i-1][j-1] += 1
                    result[i-1][j] += 1
                    result[i-1][j+1] += 1
                    result[i][j+1] += 1
                    result[i+1][j+1] += 1
                    result[i+1][j] += 1
                    result[i+1][j-1] += 1
                    result[i][j-1] += 1
                    
    return result
                
