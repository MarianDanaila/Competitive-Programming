t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    matrix = []
    for i in range(n):
        row = []
        for ch in input():
            row.append(ch)
        matrix.append(row)
    downs = 0
    rights = 0
    for i in range(n-1):
        if matrix[i][-1] != 'D':
            downs += 1
    for i in matrix[-1]:
        if i != 'R' and i != 'C':
            rights += 1
    print(downs+rights)