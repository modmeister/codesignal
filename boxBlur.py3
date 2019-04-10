def boxBlur(image):
    width = len(image[0])
    height = len(image)
    result = []
    for i in range(1, height - 1):
        temp = []
        for j in range(1, width - 1):
            total = image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] + image[i][j-1] + image[i][j] + image[i][j+1] + image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            temp.append(total // 9)
        result.append(temp)
    return result
