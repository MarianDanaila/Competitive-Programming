def countSquares(matrix):
    squares = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                squares += matrix[i][j]
            else:
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
                squares += matrix[i][j]
    return squares

print(countSquares([[0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]]))