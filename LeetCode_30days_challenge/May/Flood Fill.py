def floodFill(image, sr, sc, newColor):
    aux = image[sr][sc]
    dct = {}
    for i in range(len(image)):
        for j in range(len(image[0])):
            dct[str(i) + " " + str(j)] = True
    return paint(image, sr, sc, aux, newColor, dct)

def paint(image, i, j, first_color, newColor, dct):
    dct[str(i) + " " + str(j)] = False
    if i == 0:
        if image[i+1][j] == first_color and dct[str(i+1) + " " + str(j)]:
            image[i+1][j] = newColor
            paint(image, i + 1, j, first_color, newColor, dct)
    elif i == len(image)-1:
        if image[i-1][j] == first_color and dct[str(i-1) + " " + str(j)]:
            image[i-1][j] = newColor
            paint(image, i - 1, j, first_color, newColor, dct)
    else:
        if image[i+1][j] == first_color and dct[str(i+1) + " " + str(j)]:
            image[i+1][j] = newColor
            paint(image, i + 1, j, first_color, newColor, dct)
        if image[i-1][j] == first_color and dct[str(i+1) + " " + str(j)]:
            image[i-1][j] = newColor
            paint(image, i - 1, j, first_color, newColor, dct)
    if j == 0:
        if image[i][j+1] == first_color and dct[str(i) + " " + str(j+1)]:
            image[i][j+1] = newColor
            paint(image, i, j + 1, first_color, newColor, dct)
    elif j == len(image[0])-1:
        if image[i][j-1] == first_color and dct[str(i) + " " + str(j-1)]:
            image[i][j-1] = newColor
            paint(image, i, j - 1, first_color, newColor, dct)
    else:
        if image[i][j+1] == first_color and dct[str(i) + " " + str(j+1)]:
            image[i][j+1] = newColor
            paint(image, i, j + 1, first_color, newColor, dct)
        if image[i][j-1] == first_color and dct[str(i) + " " + str(j-1)]:
            image[i][j-1] = newColor
            paint(image, i, j - 1, first_color, newColor, dct)
    return image
print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))