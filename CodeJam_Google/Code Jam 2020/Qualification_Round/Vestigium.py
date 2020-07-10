def trace(matrix):
    r = 0
    trace = 0
    index = 0
    for row in matrix:
        if len(row) != len(set(row)):
            r += 1
        trace += row[index]
        index += 1
    return [r, trace]

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    matrix = []
    matrix_reversed = []
    for j in range(n):
        matrix.append([int(s) for s in input().split(" ")])
   

    for col in range(len(matrix)):
        column = []
        for row in range(len(matrix)):
            column.append(matrix[row][col])
        matrix_reversed.append(column)
    trace(matrix_reversed)
    print("Case #{}: {} {} {}".format(i, trace(matrix)[1], trace(matrix)[0], trace(matrix_reversed)[0]))

