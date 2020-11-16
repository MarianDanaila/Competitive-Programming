t = int(input())
for test in range(1, t+1):
    n = int(input())
    diagonals = [0] * (2*n - 1)
    matrix = []
    for i in range(n):
        row = [int(s) for s in input().split(" ")]
        matrix.append(row)

    for i in range(n):
        for j in range(n):
            diagonals[i-j+n-1] += matrix[i][j]

    print("Case #{}: {}".format(test, max(diagonals)))