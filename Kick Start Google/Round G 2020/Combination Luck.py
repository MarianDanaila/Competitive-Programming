t = int(input())
for test in range(1, t+1):
    w, n = [int(s) for s in input().split(" ")]
    x = [int(s) for s in input().split(" ")]
    min_moves = float("inf")
    for wheel in x:
        moves = 0
        for j in range(w):
            moves += min(abs(x[j]-wheel), n-(abs(x[j]-wheel)))
        min_moves = min(min_moves, moves)
    print("Case #{}: {}".format(test, min_moves))
